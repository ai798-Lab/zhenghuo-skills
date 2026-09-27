"""Relationship-specific layouts. Shared visual style does not imply shared topology."""
import math
import re
from drawing import Drawing, el, INK, BODY, GREEN, PURPLE, PEACH, PALE

KINDS={'tree','radial','matrix','decision','swimlane','layers','funnel','venn','table'}


def require(condition,message):
    if not condition:raise ValueError(message)


def exact_keys(obj,allowed,where):
    require(isinstance(obj,dict),where+' must be an object')
    extra=set(obj)-set(allowed)
    require(not extra,where+' has unsupported fields: '+', '.join(sorted(extra)))


def block(value,where='block'):
    exact_keys(value,{'title','lines','icon'},where)
    require(isinstance(value.get('title'),str) and value['title'].strip(),where+' needs a title')
    require(isinstance(value.get('lines',[]),list) and all(isinstance(t,str) for t in value.get('lines',[])),where+'.lines must be strings')
    if 'icon' in value:require(isinstance(value['icon'],str) and bool(value['icon']),where+'.icon must name an included icon')
    return value


def content_icon(title):
    """A conservative fallback for old inputs; authors should specify semantic icons."""
    for pattern,name in [
        ('事实|核实|检查|校对|验收|确认|采用|判断','checklist'),
        ('观点|问题|读者|讨论|沟通|表达','messages-square'),
        ('资料|收集|归档|基础|材料','folder'),
        ('证据|查证|研究|搜索|线索','search'),
        ('写|草稿|文案|段落','copy'),
        ('规划|优先|计划|目标','rocket'),
        ('图解|配图|可视化|改进|尝试|投入','chart-line'),
        ('应用|课程|报告|开头','book-open')]:
        if re.search(pattern,title):return name
    return 'puzzle'


class Page(Drawing):
    def __init__(self,f,fonts,style,header_plan,draw_header):
        super().__init__(f['title'],6000,fonts,f['mode'],f['print_width_mm'],f.get('source',''))
        self.f,self.s,self.segments=f,style,[]
        self.top=header_plan(f,fonts,style)[-1]
        draw_header(self,f,style,header_plan(f,fonts,style))
        self.semantic=[]

    def plan(self,b,w,size=None,pad=22):
        size=size or self.s['card']
        icon=b.get('icon') or (content_icon(b['title']) if b['title'] else None)
        icon_size=46 if self.mode=='book' else 52
        icon_mode=('aside' if w>=330 else 'top') if icon else None
        title_width=w-pad*2-(icon_size+18 if icon_mode=='aside' else 0)
        title=self.fonts.wrap(b['title'],title_width,size,'bold') if b['title'] else []
        body=[line for text in b.get('lines',[]) for line in self.fonts.wrap(text,w-pad*2,self.s['body'])]
        th=len(title)*(size+9);bh=len(body)*self.s['leading']
        head_h=max(th,icon_size if icon_mode=='aside' else 0)
        icon_h=icon_size+12 if icon_mode=='top' else 0
        return dict(title=title,body=body,size=size,pad=pad,icon=icon,icon_size=icon_size,icon_mode=icon_mode,
                    title_width=title_width,head_h=head_h,h=pad*2+icon_h+head_h+((12 if title else 0)+bh if body else 0))

    def draw_content_icon(self,name,x,y,size):
        self.icon(name,x,y,size)
        self.root[-1].set('data-role','content-icon')
        self.root[-1].set('data-icon',name)

    def content(self,x,y,w,h,p,center=False,name='node'):
        top=y+(h-p['h'])/2+p['pad']
        if p['icon_mode']=='top':
            self.draw_content_icon(p['icon'],x+w/2-p['icon_size']/2,top,p['icon_size'])
            top+=p['icon_size']+12
        elif p['icon_mode']=='aside':
            self.draw_content_icon(p['icon'],x+w-p['pad']-p['icon_size'],top,p['icon_size'])
        with self.zone(x+8,y+8,w-16,h-16,name):
            for j,t in enumerate(p['title']):
                self.text(x+p['pad']+p['title_width']/2 if center else x+p['pad'],top+p['size']+j*(p['size']+9),t,p['size'],'bold',anchor='middle' if center else 'start')
            yy=top+p['head_h']+(12 if p['title'] else 0)+self.s['body']
            for j,t in enumerate(p['body']):
                self.text(x+w/2 if center else x+p['pad'],yy+j*self.s['leading'],t,self.s['body'],anchor='middle' if center else 'start',fill=BODY)

    def node(self,b,x,y,w,h=None,color=None,center=False,p=None):
        p=p or self.plan(b,w);h=h or p['h']
        self.box(x,y,w,h,color or PALE[0],False)
        self.content(x,y,w,h,p,center,b['title'])
        return (x,y,w,h)

    def sketch_line(self,points,sw=3.2,stroke=INK,precise=False,track=False):
        """Bounded pen-like bows; anchors stay fixed. Track the actual curved route."""
        d=f'M{points[0][0]:g},{points[0][1]:g}'
        for i,(a,b) in enumerate(zip(points,points[1:])):
            dx,dy=b[0]-a[0],b[1]-a[1];length=math.hypot(dx,dy)
            if not length:continue
            if precise:
                d+=f' L{b[0]:g},{b[1]:g}'
                samples=[a,b]
            else:
                bend=min(5.5,length*.045)*(1 if i%2==0 else -1)
                c=((a[0]+b[0])/2-dy/length*bend,(a[1]+b[1])/2+dx/length*bend)
                d+=f' Q{c[0]:g},{c[1]:g} {b[0]:g},{b[1]:g}'
                samples=[((1-t)**2*a[0]+2*(1-t)*t*c[0]+t*t*b[0],
                          (1-t)**2*a[1]+2*(1-t)*t*c[1]+t*t*b[1]) for t in [j/12 for j in range(13)]]
            if track:self.segments.extend(zip(samples,samples[1:]))
        return self.path(d,stroke=stroke,sw=sw,data_line_style='precise' if precise else 'handdrawn')

    def sketch_polygon(self,points,fill,sw=3.3):
        shape=self.sketch_line(points+[points[0]],sw=sw)
        shape.set('d',shape.get('d')+' Z');shape.set('fill',fill)
        return shape

    def edge(self,points,arrow=True,precise=False):
        self.sketch_line(points,precise=precise,track=True)
        if arrow:
            a,b=points[-2:];length=math.hypot(b[0]-a[0],b[1]-a[1])
            if length:
                ux,uy=(b[0]-a[0])/length,(b[1]-a[1])/length
                self.sketch_line([(b[0]-ux*11-uy*7,b[1]-uy*11+ux*7),b,
                                  (b[0]-ux*11+uy*7,b[1]-uy*11-ux*7)],sw=3.2,precise=precise,track=True)

    def finish(self,end,extra_note=''):
        note='\n'.join(t for t in (extra_note,self.f.get('note','')) if t)
        lines=self.fonts.wrap(note,890,self.s['small']) if note else []
        for i,t in enumerate(lines):self.text(32,end+self.s['small']+26+i*(self.s['small']+12),t,self.s['small'],fill=BODY)
        self.h=end+42+len(lines)*(self.s['small']+12)
        require(self.h<=9000,'Figure too tall; split it into meaningful diagrams')
        self.root.set('viewBox',f'0 0 960 {self.h:g}')
        self.root.set('height',f'{self.h*self.print_width_mm/960:g}mm' if self.mode=='book' else f'{self.h:g}')
        self.root.find('{http://www.w3.org/2000/svg}rect').set('height',str(self.h))
        checks=self.validate()
        # Check actual connector segments against all rendered glyph bounds.
        def intersects(a,b,rect):
            lo,hi=0.,1.
            for origin,delta,mn,mx in [(a[0],b[0]-a[0],rect[0]-2,rect[2]+2),(a[1],b[1]-a[1],rect[1]-2,rect[3]+2)]:
                if abs(delta)<1e-9:
                    if not mn<=origin<=mx:return False
                else:
                    t1,t2=sorted(((mn-origin)/delta,(mx-origin)/delta));lo=max(lo,t1);hi=min(hi,t2)
                    if lo>hi:return False
            return True
        crossings=[t['text'] for t in self.texts for a,b in self.segments if intersects(a,b,t['bounds'])]
        require(not crossings,'Connector crosses text: '+' / '.join(crossings))
        checks['connector_text_errors']=[]
        checks['content_icon_count']=sum(1 for e in self.root if e.get('data-role')=='content-icon')
        require(checks['content_icon_count']>0,'Handdrawn style requires content icons, not only the header ornament')
        if self.mode=='book' and self.h*self.print_width_mm/960>195:
            checks['print_height_warning']='Exceeds a 195 mm illustration area; confirm page or split.'
        return self,dict(id=self.f['id'],title=self.f['title'],kind=self.f['kind'],mode=self.mode,height=self.h,
            print_width_mm=self.print_width_mm,png_width=self.f['png_width'],dpi=self.f['dpi'],source=self.f.get('source',''),
            intent=self.f.get('intent',''),selection_reason=self.f.get('selection_reason',''),checks=checks,texts=self.texts,relationships=self.semantic)


def tree(p,data):
    exact_keys(data,{'nodes'},'tree.data');nodes=data.get('nodes')
    require(isinstance(nodes,list) and 2<=len(nodes)<=18,'Tree needs 2–18 nodes')
    index={};children={}
    for n in nodes:
        exact_keys(n,{'id','parent','title','lines','icon'},'tree.node')
        block({k:v for k,v in n.items() if k in ('title','lines','icon')})
        require(isinstance(n.get('id'),str) and n['id'] and n['id'] not in index,'Tree IDs must be unique')
        index[n['id']]=n;children[n['id']]=[]
    roots=[n['id'] for n in nodes if not n.get('parent')]
    require(len(roots)==1,'Tree must have exactly one root')
    for n in nodes:
        if n.get('parent'):
            require(n['parent'] in index,'Unknown tree parent')
            children[n['parent']].append(n['id'])
    depth={};spans={};seen=set();leafcount=0
    def visit(key,d):
        nonlocal leafcount
        require(key not in seen,'Tree contains a cycle or repeated parent');seen.add(key);depth[key]=d
        if not children[key]:spans[key]=(leafcount,leafcount);leafcount+=1
        else:
            for child in children[key]:visit(child,d+1)
            spans[key]=(spans[children[key][0]][0],spans[children[key][-1]][1])
    visit(roots[0],0)
    require(len(seen)==len(nodes),'Tree has disconnected nodes or a cycle')
    require(leafcount<=(4 if p.mode=='book' else 3),'Too many leaves at this reading width; split the tree')
    w=min(360,(896-(leafcount-1)*28)/leafcount);slot=896/leafcount
    plans={k:p.plan(index[k],w) for k in index};rh={d:max(plans[k]['h'] for k in index if depth[k]==d) for d in set(depth.values())}
    ys={};y=p.top+12
    for d in sorted(rh):ys[d]=y;y+=rh[d]+76
    boxes={k:(32+((spans[k][0]+spans[k][1])/2+.5)*slot-w/2,ys[depth[k]],w,rh[depth[k]]) for k in index}
    for key in index:
        for child in children[key]:
            a=boxes[key];b=boxes[child];middle=(a[1]+a[3]+b[1])/2
            p.edge([(a[0]+w/2,a[1]+a[3]+4),(a[0]+w/2,middle),(b[0]+w/2,middle),(b[0]+w/2,b[1]-4)],False)
            p.semantic.append({'parent':key,'child':child})
    for key,b in boxes.items():p.node(index[key],*b,color=PALE[depth[key]%6],center=True,p=plans[key])
    return p.finish(y-76)


def radial(p,data):
    exact_keys(data,{'center','items'},'radial.data');center=block(data.get('center'));items=data.get('items')
    require(isinstance(items,list) and 3<=len(items)<=6,'Radial needs 3–6 spokes')
    for it in items:block(it)
    w=248;plans=[p.plan(it,w) for it in items];h=max(q['h'] for q in plans)
    ry=max(290,h+135);cx,cy=480,p.top+h/2+ry+20
    cp=p.plan(center,210,p.s['card'],pad=14);r=max(113,cp['h']*.64)
    require(r<155,'Radial center is too long; use a shorter central concept')
    p.blob(cx,cy,r,r,'#E6D4FF',3.2)
    p.content(cx-105,cy-cp['h']/2,210,cp['h'],cp,True,'central concept')
    for i,(it,q) in enumerate(zip(items,plans)):
        angle=-math.pi/2+2*math.pi*i/len(items)
        tx,ty=cx+320*math.cos(angle),cy+ry*math.sin(angle)
        dx,dy=tx-cx,ty-cy;length=math.hypot(dx,dy)
        clip=min(w/2/abs(dx) if dx else 1000,h/2/abs(dy) if dy else 1000)
        p.edge([(cx+dx*(r+5)/length,cy+dy*(r+5)/length),(tx-dx*clip*1.04,ty-dy*clip*1.04)],False)
        p.node(it,tx-w/2,ty-h/2,w,h,color=PALE[i%6],center=True,p=q)
        p.semantic.append({'center':center['title'],'spoke':it['title']})
    return p.finish(cy+ry+h/2+16)


def matrix(p,data):
    exact_keys(data,{'x','y','quadrants'},'matrix.data')
    for axis in ('x','y'):
        exact_keys(data.get(axis),{'title','low','high'},'matrix.'+axis)
        require(all(isinstance(data[axis].get(k),str) and data[axis][k] for k in ('title','low','high')),'Each axis needs title/low/high')
    qs=data.get('quadrants');require(isinstance(qs,dict) and set(qs)=={'tl','tr','bl','br'},'Matrix needs tl/tr/bl/br quadrants')
    w=364;plans={k:p.plan(block(v),w,pad=22) for k,v in qs.items()};h=max(q['h'] for q in plans.values())+14
    x,y=176,p.top+64;gap=20
    p.text(138,y-27,data['y']['title'],p.s['small'],'bold')
    for i,k in enumerate(('tl','tr','bl','br')):
        xx=x+(i%2)*(w+gap);yy=y+(i//2)*(h+gap)
        p.box(xx,yy,w,h,PALE[i]);p.content(xx,yy,w,h,plans[k],False,k)
    bottom=y+h*2+gap
    p.edge([(145,bottom+3),(145,y-7)],precise=True)
    p.text(125,y+p.s['small'],data['y']['high'],p.s['small'],anchor='end')
    p.text(125,bottom,data['y']['low'],p.s['small'],anchor='end')
    p.edge([(x,bottom+25),(924,bottom+25)],precise=True)
    p.text(x,bottom+66,data['x']['low'],p.s['small'])
    p.text(922,bottom+66,data['x']['high'],p.s['small'],anchor='end')
    p.text(550,bottom+110,data['x']['title'],p.s['small'],'bold',anchor='middle')
    p.semantic.append({'axes':data['x']['title']+' / '+data['y']['title'],'quadrants':list(qs)})
    return p.finish(bottom+126)


def decision(p,data):
    exact_keys(data,{'question','branches'},'decision.data');question=block(data.get('question'))
    branches=data.get('branches');require(isinstance(branches,list) and len(branches) in (2,3),'Decision needs 2 or 3 explicit branches')
    require(p.mode=='book' or len(branches)==2,'Three-way mobile decision: split or use a wider format')
    for it in branches:
        exact_keys(it,{'label','title','lines','icon'},'decision.branch');block({k:v for k,v in it.items() if k!='label'})
        require(isinstance(it.get('label'),str) and it['label'],'Every branch needs its condition label')
    labels=[it['label'] for it in branches];require(len(set(labels))==len(labels),'Branch labels must be distinct')
    qp=p.plan(question,246,pad=14);dh=max(200,qp['h']*2.25);cx=480;cy=p.top+dh/2
    p.sketch_polygon([(cx,cy-dh/2),(cx+250,cy),(cx,cy+dh/2),(cx-250,cy)],PALE[0])
    p.content(cx-123,cy-qp['h']/2,246,qp['h'],qp,True,'decision')
    n=len(branches);w=(896-52*(n-1))/n;plans=[p.plan(it,w) for it in branches];h=max(q['h'] for q in plans)
    split=cy+dh/2+34;top=split+126
    p.edge([(cx,cy+dh/2+4),(cx,split)],False)
    for i,(it,q) in enumerate(zip(branches,plans)):
        x=32+i*(w+52);target=x+w/2
        p.edge([(cx,split),(target,split),(target,top-11)])
        # Labels sit beside, not on top of, the branch connector.
        label_lines=p.fonts.wrap(it['label'],w/2-22,p.s['small'])
        require(len(label_lines)<=2,'Decision condition label too long')
        for j,t in enumerate(label_lines):p.text(target+16,split+44+j*(p.s['small']+7),t,p.s['small'],'bold')
        p.node(it,x,top,w,h,color=PALE[(i+1)%6],center=True,p=q)
        p.semantic.append({'question':question['title'],'condition':it['label'],'result':it['title']})
    return p.finish(top+h)


def swimlane(p,data):
    exact_keys(data,{'lanes','events'},'swimlane.data');lanes=data.get('lanes');events=data.get('events')
    require(isinstance(lanes,list) and 2<=len(lanes)<=3 and all(isinstance(t,str) and t for t in lanes),'Swimlane needs 2–3 named lanes')
    require(len(set(lanes))==len(lanes),'Lane names must be distinct')
    require(p.mode=='book' or len(lanes)==2,'Three lanes need a wider format; mobile should split without losing ownership')
    require(isinstance(events,list) and 2<=len(events)<=8,'Swimlane needs 2–8 sequential events')
    lane_w=896/len(lanes);node_w=lane_w-32;plans=[]
    for i,e in enumerate(events):
        exact_keys(e,{'lane','title','lines','icon'},'swimlane.event');block({k:v for k,v in e.items() if k!='lane'})
        require(e.get('lane') in lanes,'Unknown event owner: '+str(e.get('lane')))
        plans.append(p.plan(dict(title=f'{i+1:02d}  '+e['title'],lines=e.get('lines',[]),icon=e.get('icon') or content_icon(e['title'])),node_w))
    header_h=max(len(p.fonts.wrap(t,lane_w-28,p.s['card'],'bold')) for t in lanes)*(p.s['card']+9)+36
    top=p.top+header_h+16;bottom=top+sum(q['h'] for q in plans)+56*(len(events)-1)+24
    for i,lane in enumerate(lanes):
        x=32+i*lane_w
        p.sketch_polygon([(x,p.top),(x+lane_w-3,p.top),(x+lane_w-3,bottom),(x,bottom)],PALE[i%6],sw=2.6)
        for j,t in enumerate(p.fonts.wrap(lane,lane_w-28,p.s['card'],'bold')):
            p.text(x+lane_w/2,p.top+24+p.s['card']+j*(p.s['card']+9),t,p.s['card'],'bold',anchor='middle')
        p.sketch_line([(x+5,p.top+header_h),(x+lane_w-8,p.top+header_h)],stroke='#8B917E',sw=1.8)
    boxes=[];y=top
    for e,q in zip(events,plans):
        boxes.append((48+lanes.index(e['lane'])*lane_w,y,node_w,q['h']));y+=q['h']+56
    for a,b in zip(boxes,boxes[1:]):
        mid=(a[1]+a[3]+b[1])/2
        p.edge([(a[0]+a[2]/2,a[1]+a[3]+4),(a[0]+a[2]/2,mid),(b[0]+b[2]/2,mid),(b[0]+b[2]/2,b[1]-8)])
    for i,(e,q,b) in enumerate(zip(events,plans,boxes)):
        p.node(dict(title=f'{i+1:02d}  '+e['title'],lines=e.get('lines',[])),*b,color='#FFFFFF',p=q)
        p.semantic.append({'order':i+1,'owner':e['lane'],'event':e['title']})
    return p.finish(bottom)


def layers(p,data):
    exact_keys(data,{'layers'},'layers.data');items=data.get('layers')
    require(isinstance(items,list) and 2<=len(items)<=5,'Layer stack needs 2–5 layers, ordered from top to bottom')
    y=p.top+10
    for i,it in enumerate(items):
        block(it)
        left=p.plan({'title':it['title'],'icon':it.get('icon') or content_icon(it['title'])},254,pad=20)
        right=p.plan({'title':'','lines':it.get('lines',[])},590,pad=20)
        h=max(left['h'],right['h'],120)
        p.sketch_polygon([(48,y),(912,y),(912,y+h),(48,y+h)],PALE[i%6])
        p.sketch_line([(322,y+18),(322,y+h-18)],stroke='#929884',sw=1.8)
        p.content(58,y,254,h,left,True,it['title'])
        p.content(322,y,590,h,right,False,it['title']+' details')
        p.semantic.append({'layer_from_top':i+1,'name':it['title']});y+=h+10
    return p.finish(y-10)


def funnel(p,data):
    exact_keys(data,{'stages','schematic'},'funnel.data');items=data.get('stages')
    require(data.get('schematic') is True,'Funnel renderer is qualitative; set schematic=true. Use measured bars for real counts.')
    require(isinstance(items,list) and 3<=len(items)<=5,'Qualitative funnel needs 3–5 filtering stages')
    y=p.top+12;n=len(items)
    for i,it in enumerate(items):
        block(it);w1=870-i*390/n;w2=870-(i+1)*390/n
        q=p.plan(it,w2-30);h=max(q['h']+12,126);x1=(960-w1)/2;x2=(960-w2)/2
        p.sketch_polygon([(x1,y),(960-x1,y),(960-x2,y+h),(x2,y+h)],PALE[i%6])
        p.content(480-(w2-30)/2,y,w2-30,h,q,True,it['title'])
        p.semantic.append({'filter_order':i+1,'stage':it['title'],'quantitative_width':False});y+=h+12
    return p.finish(y-12,'示意：收窄表示逐层筛选，不代表数量或转化率。')


def venn(p,data):
    exact_keys(data,{'left','right','intersection'},'venn.data')
    for side in ('left','right'):
        exact_keys(data.get(side),{'title','only','icon'},'venn.'+side)
        require(isinstance(data[side].get('title'),str) and data[side]['title'],'Venn sets need titles')
        require(isinstance(data[side].get('only'),list) and all(isinstance(t,str) for t in data[side]['only']),'Venn only must contain exclusive-region strings')
        if 'icon' in data[side]:require(isinstance(data[side]['icon'],str) and bool(data[side]['icon']),'Venn icon must name an included icon')
    overlap=block(data.get('intersection'));cy=p.top+320
    p.blob(330,cy,276,258,PALE[0],3.3);p.root[-1].set('fill-opacity','0.70')
    p.blob(630,cy,276,258,PALE[1],3.3);p.root[-1].set('fill-opacity','0.70')
    # Set titles above the circles; region content is placed in exclusive / shared zones.
    for side,cx in [('left',266),('right',694)]:
        titles=p.fonts.wrap(data[side]['title'],360,p.s['card'],'bold')
        require(len(titles)<=2,'Venn set title too long')
        for j,t in enumerate(titles):p.text(cx,p.top+25+j*(p.s['card']+9),t,p.s['card'],'bold',anchor='middle')
    lp=p.plan({'title':'','lines':data['left']['only'],'icon':data['left'].get('icon') or content_icon(data['left']['title'])},218,pad=14)
    rp=p.plan({'title':'','lines':data['right']['only'],'icon':data['right'].get('icon') or content_icon(data['right']['title'])},218,pad=14)
    cp=p.plan(overlap,224,pad=12)
    require(max(lp['h'],rp['h'],cp['h'])<=280,'Venn region text is too long; move detail to a legend or use a comparison table')
    for x,w,q,name,centers in [(88,218,lp,'left exclusive',[330]),(654,218,rp,'right exclusive',[630]),(368,224,cp,'intersection',[330,630])]:
        nt,ni=len(p.texts),len(p.obstacles)
        p.content(x,cy-q['h']/2,w,q['h'],q,True,name)
        # Conservative inset ellipses ensure new icons and glyphs stay in their real regions.
        for b in [t['bounds'] for t in p.texts[nt:]]+[o['bounds'] for o in p.obstacles[ni:]]:
            for cx in centers:
                require(all(((xx-cx)/268)**2+((yy-cy)/250)**2<1 for xx in (b[0],b[2]) for yy in (b[1],b[3])),
                        'Venn '+name+' content exceeds its region; shorten labels or move detail outside')
    p.semantic.append({'sets':[data['left']['title'],data['right']['title']],'intersection':overlap['title'],'area_encodes_quantity':False})
    return p.finish(cy+280,'交集表示同时满足两个条件，圆面积不代表数量。')


def table(p,data):
    exact_keys(data,{'columns','rows','column_icons'},'table.data');columns=data.get('columns');rows=data.get('rows')
    require(isinstance(columns,list) and len(columns)==2 and all(isinstance(t,str) and t for t in columns),'Table needs exactly two named alternatives')
    require(isinstance(rows,list) and 1<=len(rows)<=8,'Comparison table needs 1–8 aligned dimensions')
    icons=data.get('column_icons',[content_icon(t) for t in columns])
    require(isinstance(icons,list) and len(icons)==2 and all(isinstance(t,str) and t for t in icons),'column_icons must name two included icons')
    for row in rows:
        exact_keys(row,{'dimension','values'},'table.row')
        require(isinstance(row.get('dimension'),str) and row['dimension'],'Each row needs its comparison dimension')
        require(isinstance(row.get('values'),list) and len(row['values'])==2 and all(isinstance(v,str) for v in row['values']),'Each comparison dimension needs two values')
    widths=[214,341,341];xs=[32,246,587];y=p.top+12
    all_rows=[['比较维度',*columns]]+[[r['dimension'],*r['values']] for r in rows]
    for ri,cells in enumerate(all_rows):
        size=p.s['card'] if ri==0 else p.s['body'];gap=size+12
        wraps=[p.fonts.wrap(t,widths[i]-36,size,'bold' if ri==0 or i==0 else 'regular') for i,t in enumerate(cells)]
        icon_size=46 if p.mode=='book' else 52
        icon_h=icon_size+12 if ri==0 else 0
        h=38+icon_h+max(len(lines) for lines in wraps)*gap
        for ci,lines in enumerate(wraps):
            color=PALE[ci] if ri==0 else '#FFFFFF' if ri%2==0 else '#F6F8F0'
            p.rect(xs[ci],y,widths[ci],h,color)
            if ri==0:p.draw_content_icon((['chart-line']+icons)[ci],xs[ci]+18,y+18,icon_size)
            with p.zone(xs[ci]+12,y+10,widths[ci]-24,h-20,'comparison cell'):
                for j,t in enumerate(lines):p.text(xs[ci]+18,y+icon_h+22+size+j*gap,t,size,'bold' if ri==0 or ci==0 else 'regular')
        p.sketch_line([(32,y+h),(928,y+h)],stroke='#858B77',sw=1.8)
        y+=h
    for x in (246,587):p.sketch_line([(x,p.top+12),(x,y)],stroke='#858B77',sw=1.8)
    p.sketch_line([(32,p.top+12),(928,p.top+12),(928,y),(32,y),(32,p.top+12)],sw=3.1)
    p.semantic.extend({'dimension':r['dimension'],'alternatives':columns,'values':r['values']} for r in rows)
    return p.finish(y)


BUILDERS={'tree':tree,'radial':radial,'matrix':matrix,'decision':decision,'swimlane':swimlane,'layers':layers,'funnel':funnel,'venn':venn,'table':table}


def build_structure(f,fonts,settings,header_plan,draw_header):
    require('data' in f,f['kind']+' needs relationship-specific data')
    p=Page(f,fonts,settings(f['mode']),header_plan,draw_header)
    return BUILDERS[f['kind']](p,f['data'])
