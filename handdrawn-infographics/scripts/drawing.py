"""Editable SVG primitives for the approved handdrawn infographic style."""
from pathlib import Path
from functools import lru_cache
from contextlib import contextmanager
import copy
import math
import re
import xml.etree.ElementTree as ET

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
INK, BODY = '#1B1C18', '#32352E'
GREEN, PURPLE, PEACH, TEAL = '#D5F548', '#B591EF', '#FFC5A4', '#9DDDD0'
PALE = ['#F0F8CF', '#ECE2FC', '#DCF3EB', '#EEE5FC', '#FFE9DC', '#EBF6CB']
COLORS = [GREEN, PURPLE, TEAL, PURPLE, PEACH, GREEN]
ASSETS = Path(__file__).resolve().parents[1] / 'assets'
CUSTOM_ICONS = {
    'folder': ['M2.8 7.4 Q2.5 4.6 4.6 4.8 L9.1 4.5 Q10.7 4.6 12 7.5 Q17 7.1 21 7.5 L20.6 20.1 Q11.9 19.6 3.1 20.3 Z', 'M3 9.6 Q11.9 9.1 20.8 9.5'],
    'checklist': ['M7 3.5 Q13 3 20.2 3.6 L19.7 21 Q12.9 20.4 5 21.3 L5.3 5.8', 'M2.4 8.1 L4 9.6 L7.8 5.6', 'M9.8 8 Q13 7.6 16.5 8.1', 'M8.4 13 Q13 12.6 17 13.2', 'M8.6 17.8 Q11.7 17.2 15.6 17.8']
}


def el(tag, **attrs):
    e = ET.Element('{' + NS + '}' + tag)
    for k, v in attrs.items():
        if v is not None:
            e.set(k.replace('_', '-'), str(v))
    return e


class FontMetrics:
    def __init__(self, regular, bold):
        self.paths = {'regular': Path(regular).resolve(), 'bold': Path(bold).resolve()}
        self.fonts = {k: TTFont(str(v)) for k, v in self.paths.items()}
        names = [f['name'].getDebugName(16) or f['name'].getDebugName(1) for f in self.fonts.values()]
        if names[0] != names[1]:
            raise ValueError('Regular and Bold must belong to the same font family')
        self.family = names[0]

    @lru_cache(maxsize=32768)
    def glyph(self, ch, weight):
        f = self.fonts[weight]
        name = f.getBestCmap().get(ord(ch))
        if not name:
            raise ValueError(f'Font lacks character {ch!r} U+{ord(ch):04X}')
        gs = f.getGlyphSet()
        pen = BoundsPen(gs)
        gs[name].draw(pen)
        return f['hmtx'][name][0], pen.bounds, f['head'].unitsPerEm

    @lru_cache(maxsize=16384)
    def measure(self, text, size, weight='regular'):
        cursor, boxes = 0, []
        for ch in text:
            advance, box, upm = self.glyph(ch, weight)
            if box:
                a, b, c, d = box
                boxes.append(((cursor+a)*size/upm, -d*size/upm, (cursor+c)*size/upm, -b*size/upm))
            cursor += advance
        bounds = (min(x[0] for x in boxes), min(x[1] for x in boxes), max(x[2] for x in boxes), max(x[3] for x in boxes)) if boxes else (0, 0, 0, 0)
        return cursor*size/upm if text else 0, bounds

    def width(self, text, size, weight='regular'):
        return self.measure(text, size, weight)[0]

    def wrap(self, text, maxwidth, size, weight='regular'):
        """Keep Latin tokens together when possible; preserve every nonspace character."""
        result = []
        for para in text.split('\n'):
            paragraph_start = len(result)
            tokens = re.findall(r'[A-Za-z0-9_./~:@#+=\-]+|\s+|.', para)
            line = ''
            for token in tokens:
                if self.width(token, size, weight) > maxwidth:
                    # Prefer the visible separators of long code identifiers.
                    chunks = re.findall(r'[^/_.\-]+[/_.\-]?|[/_.\-]', token)
                    parts = [part for chunk in chunks for part in (list(chunk) if self.width(chunk, size, weight)>maxwidth else [chunk])]
                else:
                    parts = [token]
                for part in parts:
                    if line and self.width(line+part, size, weight) > maxwidth:
                        if part[:1] in '，。；：、）】》！？,.!?;:)]' and len(line) > 1:
                            result.append(line[:-1].rstrip())
                            line = line[-1]+part
                        else:
                            result.append(line.rstrip())
                            line = part.lstrip()
                    else:
                        line += part
            result.append(line.rstrip())
            # A final lone Chinese character is legible but visually jarring.
            # Rebalance without deleting characters or reducing the type size.
            while len(result)-paragraph_start>=2 and result[-1] and self.width(re.sub(r'[，。；：、）】》！？,.!?;:)\]]','',result[-1]),size,weight)<size*1.85:
                previous=result[-2].rstrip()
                pieces=re.findall(r'[A-Za-z0-9_./~:@#+=\-]+|\s+|.',previous)
                if len(pieces)<2:break
                move=pieces[-1];head=previous[:-len(move)].rstrip()
                candidate=move+(' ' if re.search(r'[A-Za-z0-9]$',move) and re.match(r'[A-Za-z0-9]',result[-1]) else '')+result[-1]
                if not head or self.width(candidate,size,weight)>maxwidth:break
                result[-2],result[-1]=head,candidate
        return result


class Drawing:
    def __init__(self, title, height, fonts, mode='article', print_width_mm=144, source=''):
        self.fonts, self.h, self.mode = fonts, height, mode
        self.texts, self.obstacles, self.active_zone = [], [], None
        self.print_width_mm = print_width_mm
        self.root = el('svg', width=f'{print_width_mm:g}mm' if mode == 'book' else '960',
                       height=f'{height*print_width_mm/960:g}mm' if mode == 'book' else f'{height:g}',
                       viewBox=f'0 0 960 {height:g}', role='img', aria_label=title,
                       data_text_editable='true', font_kerning='none', font_variant_ligatures='none')
        t = el('title'); t.text = title; self.root.append(t)
        d = el('desc'); d.text = f'彩色手绘信息图。文字为可编辑 SVG text。来源：{source or "当前用户提供的内容"}。'; self.root.append(d)
        self.root.append(ET.Comment('Icon geometry: sketchyicons, derived from Lucide/Feather. See accompanying NOTICE-sketchyicons.txt.'))
        self.rect(0, 0, 960, height, '#FFFFFF')

    def path(self, d, fill='none', stroke=INK, sw=3, **attrs):
        e = el('path', d=d, fill=fill, stroke=stroke, stroke_width=sw,
               stroke_linecap='round', stroke_linejoin='round', **attrs)
        self.root.append(e)
        return e

    def rect(self, x, y, w, h, fill):
        self.root.append(el('rect', x=x, y=y, width=w, height=h, fill=fill))

    def text(self, x, y, text, size=26, weight='regular', anchor='start', fill=INK):
        if not text:
            return
        advance, box = self.fonts.measure(text, size, weight)
        tx = x - (advance/2 if anchor == 'middle' else advance if anchor == 'end' else 0)
        e = el('text', id=f'text-{len(self.texts)+1:03d}', x=x, y=y, font_family=self.fonts.family,
               font_size=size, font_weight=700 if weight == 'bold' else 400, fill=fill, text_anchor=anchor)
        e.text = text; self.root.append(e)
        self.texts.append({'text': text, 'size': size, 'bounds': [tx+box[0], y+box[1], tx+box[2], y+box[3]], 'zone': self.active_zone})

    @contextmanager
    def zone(self, x, y, w, h, name):
        previous = self.active_zone
        self.active_zone = {'name': name, 'bounds': [x, y, x+w, y+h]}
        try:
            yield
        finally:
            self.active_zone = previous

    def blob(self, cx, cy, rx, ry, fill, sw=0):
        self.path(f'M{cx-rx},{cy+1} C{cx-rx-4},{cy-ry*.72} {cx-rx*.45},{cy-ry-3} {cx+3},{cy-ry} C{cx+rx*.85},{cy-ry-2} {cx+rx+3},{cy-ry*.3} {cx+rx},{cy+2} C{cx+rx},{cy+ry*.9} {cx+rx*.2},{cy+ry+3} {cx-3},{cy+ry} C{cx-rx*.8},{cy+ry+1} {cx-rx+2},{cy+ry*.35} {cx-rx},{cy+1} Z', fill, INK if sw else 'none', sw)

    def box(self, x, y, w, h, fill, puzzle=False, notch=False):
        if not puzzle:
            self.path(f'M{x+12},{y+1} C{x+w*.28},{y-2} {x+w*.7},{y+3} {x+w-12},{y} Q{x+w+1},{y+1} {x+w},{y+14} C{x+w-2},{y+h*.38} {x+w+2},{y+h*.73} {x+w},{y+h-12} Q{x+w-1},{y+h+1} {x+w-14},{y+h} C{x+w*.7},{y+h+2} {x+w*.3},{y+h-2} {x+12},{y+h} Q{x-1},{y+h} {x},{y+h-12} C{x+2},{y+h*.68} {x-2},{y+h*.3} {x},{y+12} Q{x},{y} {x+12},{y+1} Z', fill, sw=3.3)
            return
        cy=min(101, h*.5); lo=cy-13; hi=cy+13
        if notch:
            shape=f'M{x+12},{y} Q{x+w*.5},{y+2} {x+w-12},{y} Q{x+w+1},{y} {x+w},{y+12} Q{x+w-2},{y+h*.5} {x+w},{y+h-12} Q{x+w},{y+h+1} {x+w-12},{y+h} Q{x+w*.4},{y+h+2} {x+12},{y+h} Q{x},{y+h} {x},{y+h-12} L{x},{y+hi} C{x+29},{y+hi+10} {x+31},{y+lo-10} {x},{y+lo} L{x},{y+12} Q{x},{y} {x+12},{y} Z'
        else:
            shape=f'M{x+12},{y} Q{x+w*.45},{y-2} {x+w-12},{y+1} Q{x+w+1},{y} {x+w},{y+12} L{x+w},{y+lo} C{x+w+29},{y+lo-10} {x+w+31},{y+hi+10} {x+w},{y+hi} L{x+w},{y+h-12} Q{x+w},{y+h+1} {x+w-12},{y+h} Q{x+w*.4},{y+h-2} {x+12},{y+h+1} Q{x-1},{y+h} {x},{y+h-12} Q{x+2},{y+h*.5} {x},{y+12} Q{x},{y} {x+12},{y} Z'
        self.path(shape, fill, sw=3.3)

    def arrow(self, x1, y1, x2, y2, sw=3):
        dx, dy = x2-x1, y2-y1
        length=math.hypot(dx, dy)
        if length < 2:
            return
        ux, uy = dx/length, dy/length; px, py = -uy, ux
        self.path(f'M{x1},{y1} Q{(x1+x2)/2+px*1.5},{(y1+y2)/2+py*1.5} {x2},{y2}', sw=sw)
        self.path(f'M{x2-ux*10+px*7},{y2-uy*10+py*7} L{x2},{y2} L{x2-ux*10-px*7},{y2-uy*10-py*7}', sw=sw)

    def icon(self, name, x, y, size=49):
        g = el('g', transform=f'translate({x} {y}) scale({size/24})', fill='none', stroke=INK,
               color=INK, stroke_width=1.6, stroke_linecap='round', stroke_linejoin='round')
        if name in CUSTOM_ICONS:
            for p in CUSTOM_ICONS[name]:
                g.append(el('path', d=p))
        else:
            p = ASSETS / 'icons' / (name+'.svg')
            if not re.fullmatch(r'[a-z0-9-]+', name) or not p.is_file():
                raise ValueError(f'Unknown icon: {name}')
            for child in ET.parse(p).getroot():
                if isinstance(child.tag, str):
                    g.append(copy.deepcopy(child))
        self.root.append(g)
        self.obstacles.append({'name': 'icon:'+name, 'bounds': [x-2, y-2, x+size+2, y+size+2]})

    def validate(self):
        errors=[]
        def overlap(a, b):
            return min(a[2],b[2])-max(a[0],b[0])>1 and min(a[3],b[3])-max(a[1],b[1])>1
        for i, t in enumerate(self.texts):
            b=t['bounds']; z=t['zone']['bounds'] if t['zone'] else [8, 8, 952, self.h-8]
            if b[0]<z[0]-0.1 or b[1]<z[1]-0.1 or b[2]>z[2]+0.1 or b[3]>z[3]+0.1:
                errors.append('Text exceeds zone: '+t['text'])
            if self.mode=='book' and t['size']*self.print_width_mm/960*72/25.4<10:
                errors.append('Book type smaller than 10 pt: '+t['text'])
            for other in self.texts[:i]:
                if overlap(b,other['bounds']):
                    errors.append('Text overlap: '+t['text']+' / '+other['text'])
            for icon in self.obstacles:
                if overlap(b,icon['bounds']):
                    errors.append('Text touches '+icon['name']+': '+t['text'])
        if errors:
            raise ValueError('\n'.join(errors))
        return {'text_count': len(self.texts), 'editable': True, 'layout_errors': [], 'visual_review': 'required'}

    def save(self, path):
        ET.indent(self.root)
        ET.ElementTree(self.root).write(path, encoding='utf-8', xml_declaration=True)
