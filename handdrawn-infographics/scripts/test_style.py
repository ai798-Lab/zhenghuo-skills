"""Regression checks for the handdrawn style; still requires visual review."""
import copy
import json
import unittest
from pathlib import Path

from build import build, normalize, font_path
from drawing import FontMetrics, NS


class HanddrawnStyleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fonts = FontMetrics(font_path(None, 'Regular'), font_path(None, 'Bold'))
        cls.doc = json.loads((Path(__file__).resolve().parents[1] / 'assets/examples/structures.json').read_text())

    def test_each_structure_has_icons_in_its_content(self):
        def without_icons(value):
            if isinstance(value,dict):return {k:without_icons(v) for k,v in value.items() if k not in ('icon','column_icons')}
            if isinstance(value,list):return [without_icons(v) for v in value]
            return value
        for figure in normalize(without_icons(self.doc)):
            with self.subTest(kind=figure['kind']):
                drawing, _ = build(figure, self.fonts)
                icons = [o for o in drawing.obstacles if o['name'].startswith('icon:')]
                self.assertGreater(len(icons), 1, 'Only the decorative header icon survives')

    def test_tree_connectors_have_visible_curvature(self):
        figure = next(f for f in normalize(self.doc) if f['kind'] == 'tree')
        drawing, _ = build(figure, self.fonts)
        connectors = [p for p in drawing.root.findall('{'+NS+'}path')
                      if p.get('fill') == 'none' and p.get('stroke') != 'none']
        self.assertTrue(connectors)
        self.assertTrue(all('Q' in p.get('d', '') or 'C' in p.get('d', '') for p in connectors),
                        'Tree links fell back to rigid polylines')

    def test_requested_icon_reaches_each_structure(self):
        for original in self.doc['figures']:
            f = copy.deepcopy(original)
            kind, data = f['kind'], f['data']
            target = {'tree': lambda: data['nodes'][0], 'radial': lambda: data['center'],
                      'matrix': lambda: data['quadrants']['tl'], 'decision': lambda: data['question'],
                      'swimlane': lambda: data['events'][0], 'layers': lambda: data['layers'][0],
                      'funnel': lambda: data['stages'][0], 'venn': lambda: data['intersection']}
            if kind == 'table':
                data['column_icons'] = ['rocket', 'book-open']
            else:
                target[kind]()['icon'] = 'rocket'
            with self.subTest(kind=kind):
                try:
                    drawing, _ = build(normalize({'mode':'book', 'figures':[f]})[0], self.fonts)
                except ValueError as error:
                    self.fail('Requested content icon was rejected: '+str(error))
                self.assertTrue(any(o['name'] == 'icon:rocket' for o in drawing.obstacles))

    def test_article_venn_preserves_icons_and_reading_size(self):
        f=copy.deepcopy(next(f for f in self.doc['figures'] if f['kind']=='venn'))
        f['mode']='article'
        try:
            drawing,record=build(normalize({'figures':[f]})[0],self.fonts)
        except ValueError as error:
            self.fail('Readable Venn labels no longer fit after adding icons: '+str(error))
        self.assertEqual(record['checks']['content_icon_count'],3)
        self.assertGreaterEqual(min(t['size'] for t in drawing.texts),34)


if __name__ == '__main__':
    unittest.main()
