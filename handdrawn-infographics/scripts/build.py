#!/usr/bin/env python3
"""Build local editable SVG + PNG sets; no network and no implicit overwrites."""
import argparse
import json
import hashlib
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

from drawing import Drawing, FontMetrics, ASSETS, INK, BODY, GREEN, PEACH, PALE, COLORS
from structures import KINDS as STRUCTURE_KINDS, build_structure


def settings(mode):
    return dict(title=44, card=32, body=26, small=24, leading=35) if mode=='book' else dict(title=52, card=42, body=38, small=34, leading=51)


def header_plan(f, fonts, s):
    title=fonts.wrap(f['title'], 784, s['title'], 'bold')
    top=100 if f.get('label') else 68
    title_gap=s['title']*1.22
    last=top+(len(title)-1)*title_gap
    sub=fonts.wrap(f['subtitle'], 895, s['body']) if f.get('subtitle') else []
    sub_y=last+s['body']+18
    bottom=max(137, sub_y+(len(sub)-1)*s['leading']+36 if sub else last+42)
    return title, top, title_gap, sub, sub_y, bottom


def draw_header(d, f, s, p):
    titles, top, gap, sub, sy, _=p
    if f.get('label'):
        d.text(32, 35, f['label'], s['small'], 'bold')
    for i, text in enumerate(titles):
        y=top+i*gap; w=d.fonts.width(text, s['title'], 'bold')+10
        d.path(f'M32,{y-s["title"]*.75} Q{32+w*.5},{y-s["title"]*.9} {32+w},{y-s["title"]*.74} L{34+w},{y+8} Q{32+w*.5},{y+4} 32,{y+10} Z', GREEN, 'none', 0)
        d.text(32,y,text,s['title'],'bold')
    d.blob(875,78,51,45,'#E6D4FF')
    d.icon('puzzle',842,45,66)
    for i,text in enumerate(sub):
        d.text(32, sy+i*s['leading'], text, s['body'], fill=BODY)


def card_plan(item, w, fonts, s, numbered, notch=False):
    left=88 if numbered else 26
    title=fonts.wrap(item['title'],w-left-86,s['card'],'bold')
    label=fonts.wrap(item.get('label',''),w-52,s['small'],'bold') if item.get('label') else []
    label_h=len(label)*(s['small']+9)
    title_h=max(s['card'],len(title)*(s['card']+9))
    title_y=26+s['card']+label_h
    body_x=48 if notch else 26
    body=[]
    for line in item['lines']:
        body.extend(fonts.wrap(line,w-body_x-26,s['body']))
    body_y=title_y+title_h-s['card']+s['body']+16
    height=body_y+max(0,len(body)-1)*s['leading']+30 if body else title_y+title_h-s['card']+30
    return dict(title=title,label=label,title_y=title_y,body_y=body_y,body=body,body_x=body_x,height=max(height,124),left=left,label_h=label_h)


def draw_card(d,item,i,x,y,w,h,p,s,numbered=False,puzzle=False,notch=False):
    color=PALE[4] if item.get('human') else PALE[i%6]
    d.box(x,y,w,h,color,puzzle,notch)
    with d.zone(x+16,y+12,w-32,h-24,item['title']):
        for j,txt in enumerate(p['label']):
            d.text(x+26,y+26+s['small']+j*(s['small']+9),txt,s['small'],'bold')
        if numbered:
            cy=y+p['title_y']-s['card']*.34
            d.blob(x+45,cy,26,26,PEACH if item.get('human') else COLORS[i%6])
            d.text(x+45,cy+s['card']*.32,f'{i+1:02d}',min(s['card'],34),'bold',anchor='middle')
        for j,txt in enumerate(p['title']):
            d.text(x+p['left'],y+p['title_y']+j*(s['card']+9),txt,s['card'],'bold')
        for j,txt in enumerate(p['body']):
            d.text(x+p['body_x'],y+p['body_y']+j*s['leading'],txt,s['body'],fill=BODY)
    d.icon(item.get('icon','puzzle'),x+w-68,y+24+p['label_h'],46)


def build(f,fonts):
    if f['kind'] in STRUCTURE_KINDS:
        return build_structure(f,fonts,settings,header_plan,draw_header)
    mode=f['mode'];s=settings(mode);kind=f['kind'];items=f['items'];n=len(items)
    columns=f.get('columns',1 if mode=='article' or kind=='timeline' else 2)
    if columns not in (1,2) or kind=='timeline' and columns!=1:
        raise ValueError('columns must be 1 or 2; timeline requires 1')
    numbered=kind in ('steps','cycle')
    cycle=kind=='cycle'
    if cycle and columns==2 and n not in (4,6):
        raise ValueError('A two-column cycle needs 4 or 6 nodes; choose columns=1')
    if cycle and n<2:
        raise ValueError('A cycle needs at least two nodes')
    start=header_plan(f,fonts,s)
    # Sequential grids use row-major order. Cycles use a true clockwise order.
    order=([[0,1],[5,2],[4,3]] if n==6 else [[0,1],[3,2]]) if cycle and columns==2 else [list(range(k,min(k+columns,n))) for k in range(0,n,columns)]
    gap=64 if cycle or kind=='steps' and columns==2 else 40
    y=start[-1];positions={};plans={};rows=[]
    for indices in order:
        row=[]
        for col,i in enumerate(indices):
            full=columns==1 or len(indices)==1
            x=84 if cycle and columns==1 else 32 if full or col==0 else 520
            w=828 if cycle and columns==1 else 880 if full else 400
            notch=columns==2 and col==1 and not cycle
            p=card_plan(items[i],w,fonts,s,numbered,notch)
            row.append((i,x,w,p,notch))
        h=max(c[3]['height'] for c in row)
        for i,x,w,p,notch in row:
            positions[i]=(x,y,w,h);plans[i]=(p,notch)
        rows.append(indices);y+=h+gap
    end=y-gap
    foot=fonts.wrap(f['note'],890,s['small']) if f.get('note') else []
    height=end+(s['small']+14)*len(foot)+38
    if height>9000:
        raise ValueError('Figure too tall; split it into meaningful parts')
    d=Drawing(f['title'],height,fonts,mode,f['print_width_mm'],f.get('source',''))
    draw_header(d,f,s,start)
    for i in range(n):
        x,y,w,h=positions[i];p,notch=plans[i]
        draw_card(d,items[i],i,x,y,w,h,p,s,numbered,not cycle,notch)
    if cycle and columns==2:
        for i in range(n):
            x1,y1,w1,h1=positions[i];x2,y2,w2,h2=positions[(i+1)%n]
            if y1==y2:
                if x2>x1:d.arrow(x1+w1+10,y1+h1/2,x2-12,y2+h2/2)
                else:d.arrow(x1-10,y1+h1/2,x2+w2+12,y2+h2/2)
            elif y2>y1:d.arrow(x1+w1/2,y1+h1+10,x2+w2/2,y2-12)
            else:d.arrow(x1+w1/2,y1-10,x2+w2/2,y2+h2+12)
    elif kind in ('steps','cycle','timeline'):
        if columns==1:
            for i in range(n-1):
                x,y,w,h=positions[i];_,nexty,_,_=positions[i+1]
                d.arrow(x+w/2,y+h+9,x+w/2,nexty-10)
        else:
            for indices in rows:
                if len(indices)==2:
                    x,y,w,h=positions[indices[0]];x2,_,_,_=positions[indices[1]]
                    d.arrow(x+w+33,y+min(101,h*.5),x2-10,y+min(101,h*.5))
        if cycle:
            x,y,w,h=positions[n-1];_,top,_,first_h=positions[0]
            d.path(f'M{x-9},{y+h/2} L36,{y+h/2} L36,{top+first_h/2} L{x-28},{top+first_h/2}')
            d.arrow(x-28,top+first_h/2,x-10,top+first_h/2)
    for j,txt in enumerate(foot):
        d.text(32,end+s['small']+23+j*(s['small']+14),txt,s['small'],fill=BODY)
    checks=d.validate()
    return d,dict(id=f['id'],title=f['title'],kind=kind,mode=mode,columns=columns,height=height,
                  print_width_mm=f['print_width_mm'],png_width=f['png_width'],dpi=f['dpi'],
                  source=f.get('source',''),intent=f.get('intent',''),selection_reason=f.get('selection_reason',''),items=n,checks=checks,texts=d.texts)


def font_path(explicit,weight):
    if explicit:
        p=Path(explicit).expanduser()
        if not p.is_file():raise ValueError(f'Font not found: {p}')
        return p
    bundled=ASSETS/'fonts/Xiaolai-Regular.ttf'
    if bundled.is_file():return bundled
    raise ValueError('Bundled Xiaolai font is missing. Restore assets/fonts or pass both --font-regular and --font-bold.')


def normalize(doc):
    if not isinstance(doc,dict) or not isinstance(doc.get('figures'),list) or not doc['figures']:
        raise ValueError('figures must be a nonempty array')
    figures=[];ids=set()
    for original in doc['figures']:
        if not isinstance(original,dict):raise ValueError('Each figure must be an object')
        allowed={'id','title','kind','mode','columns','label','subtitle','note','source','items','data','intent','selection_reason','print_width_mm','dpi','png_width'}
        unknown=set(original)-allowed
        if unknown:raise ValueError('Unsupported figure fields; do not silently discard relations: '+', '.join(sorted(unknown)))
        f=dict(original)
        for k in ['mode','print_width_mm','dpi','png_width']:
            if k not in f and k in doc:f[k]=doc[k]
        f.setdefault('mode','article')
        if f['mode'] not in ('article','book'):raise ValueError('Unknown mode')
        for key in ('id','title','kind'):
            if not isinstance(f.get(key),str) or not f[key].strip():raise ValueError(f'{key} is required')
        if not re.fullmatch(r'[\w\-]+',f['id']) or f['id'] in ids:raise ValueError('Invalid or duplicate id: '+f['id'])
        ids.add(f['id'])
        if f['kind'] not in {'steps','cards','compare','cycle','timeline'}|STRUCTURE_KINDS:raise ValueError('Unknown kind: '+f['kind'])
        if f['kind'] in STRUCTURE_KINDS:
            if not isinstance(f.get('data'),dict):raise ValueError('This structure requires data with its actual relationships')
            if 'items' in f or 'columns' in f:raise ValueError('Do not flatten structured data into items/columns')
        else:
            if 'data' in f:raise ValueError('Legacy item layouts do not accept data; choose the appropriate structure')
            if not isinstance(f.get('items'),list) or not f['items']:raise ValueError('items must be a nonempty array')
        for item in f.get('items',[]):
            if not isinstance(item,dict) or not isinstance(item.get('title'),str) or not item['title']:raise ValueError('Each item needs a title')
            if not isinstance(item.get('lines'),list) or not all(isinstance(x,str) for x in item['lines']):raise ValueError('Each item needs a lines string array')
            unknown=set(item)-{'title','lines','icon','label','human'}
            if unknown:raise ValueError('Unsupported item fields: '+', '.join(sorted(unknown)))
            for k in ('label','icon'):
                if k in item and not isinstance(item[k],str):raise ValueError('Item '+k+' must be a string')
            if 'human' in item and not isinstance(item['human'],bool):raise ValueError('human must be true or false')
        for k in ('label','subtitle','note','source','intent','selection_reason'):
            if k in f and not isinstance(f[k],str):raise ValueError(k+' must be a string')
        f.setdefault('print_width_mm',144)
        f.setdefault('dpi',600 if f['mode']=='book' else 144)
        f.setdefault('png_width',round(f['print_width_mm']/25.4*f['dpi']) if f['mode']=='book' else 1440)
        for k in ('print_width_mm','dpi','png_width'):
            if not isinstance(f[k],(int,float)) or not math.isfinite(f[k]) or f[k]<=0:raise ValueError('Invalid '+k)
        f['png_width']=round(f['png_width'])
        if f['png_width']>12000:raise ValueError('PNG width exceeds practical limit')
        figures.append(f)
    return figures


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input',type=Path);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--font-regular');p.add_argument('--font-bold');p.add_argument('--node');p.add_argument('--sharp-module')
    p.add_argument('--svg-only',action='store_true');p.add_argument('--overwrite',action='store_true')
    args=p.parse_args();out=args.out.expanduser().resolve()
    if bool(args.font_regular) != bool(args.font_bold):
        raise ValueError('Pass both --font-regular and --font-bold; a single-weight font can use the same path twice.')
    figures=normalize(json.loads(args.input.read_text(encoding='utf-8')))
    fonts=FontMetrics(font_path(args.font_regular,'Regular'),font_path(args.font_bold,'Bold'))
    targets=[out/'manifest.json',out/'render-report.json',out/'NOTICE-sketchyicons.txt']
    targets += [out/ext.upper()/(f['id']+'.'+ext) for f in figures for ext in ('svg','png')]
    if fonts.bundled:
        targets += [out/'fonts'/name for name in ('Xiaolai-Regular.ttf','OFL.txt','README.md')]
    existing=[str(x) for x in targets if x.exists()]
    if existing and not args.overwrite:raise ValueError('Refusing to overwrite existing output. Use a new folder or --overwrite: '+existing[0])
    prepared=[build(f,fonts) for f in figures]  # All layouts pass before writing any output.
    for sub in ('SVG','PNG'):(out/sub).mkdir(parents=True,exist_ok=True)
    records=[]
    for drawing,record in prepared:
        svg_path=out/'SVG'/(record['id']+'.svg')
        drawing.save(svg_path)
        record['svg_sha256']=hashlib.sha256(svg_path.read_bytes()).hexdigest()
        records.append(record)
    font_files={k:str(v) for k,v in fonts.paths.items()}
    if fonts.bundled:
        (out/'fonts').mkdir(exist_ok=True)
        for name in ('Xiaolai-Regular.ttf','OFL.txt','README.md'):
            shutil.copy2(ASSETS/'fonts'/name,out/'fonts'/name)
        font_files={k:'fonts/Xiaolai-Regular.ttf' for k in fonts.paths}
    manifest={'schema':1,'style':'handdrawn-infographics B','font_family':fonts.family,
              'fonts':font_files,'font_styles':fonts.styles,'font_weights':fonts.weights,
              'embedded_webfont':fonts.bundled,'figures':records}
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    shutil.copy2(ASSETS/'NOTICE-sketchyicons.txt',out/'NOTICE-sketchyicons.txt')
    if not args.svg_only:
        node=args.node or shutil.which('node')
        if not node:
            cached=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node'
            if cached.is_file():node=str(cached)
        if not node:raise ValueError('Node.js missing; SVG generated, PNG not generated')
        command=[node,str(Path(__file__).with_name('render.cjs')),str(out/'manifest.json')]
        if args.sharp_module:command+=['--sharp-module',args.sharp_module]
        subprocess.run(command,check=True)
    print(json.dumps({'output':str(out),'svg':len(records),'png':0 if args.svg_only else len(records),'visual_review':'required'},ensure_ascii=False))


if __name__=='__main__':
    try:main()
    except (ValueError,FileNotFoundError,subprocess.CalledProcessError) as e:
        print('ERROR: '+str(e),file=sys.stderr);sys.exit(1)
