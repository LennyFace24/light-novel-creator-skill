#!/usr/bin/env python3
import argparse,os,re,sys
VR={"开篇首卷":(60000,90000),"主线正篇卷":(65000,85000),"日常过渡卷":(50000,70000),"高潮决战卷":(80000,100000)}
CMIN=3500
def dt(vd):
    sf=os.path.join(vd,f"{os.path.basename(vd)[:9]}_summary.md")
    if os.path.exists(sf):
        with open(sf)as f:
            for l in f:
                for t in VR:
                    if t in l:return t
    return"主线正篇卷"
def er(text):
    t=len(text)
    if t==0:return 1.0
    ek=['天色','阳光','微风','树叶','空气','云朵','街道','建筑','墙壁','地板','窗外','风景','景色']
    pad=0;run=0
    for s in re.split(r'[。！？]',text):
        s=s.strip()
        if not s:continue
        ha=any(w in s for w in['说','道','想','走','看','拿','放','战斗','攻击'])
        hd='「' in s or'"'in s
        ie=any(k in s for k in ek)and not ha and not hd
        run=run+1 if ie else 0
        if run>=3:pad+=len(s)
    for m in re.findall(r'(?:他|她|我|自己)[^。！？]{100,500}[。！？]',text):
        if len(m)>500:pad+=len(m)-500
    return max(0.0,(t-pad)/t)
p=argparse.ArgumentParser();p.add_argument("project_dir");p.add_argument("volume")
a=p.parse_args();vd=os.path.join(a.project_dir,a.volume)
if not os.path.isdir(vd):print(f"❌");sys.exit(1)
vid=a.volume[:9];ok=True
def r(n,pa,is_,info=False):
    global ok
    print(f"{'✅'if pa else'❌'}{n}")
    for i in is_:print(f"  {'ℹ️'if info else'⚠️'}{i}")
    if not pa and not info:ok=False
    print()
cf=os.path.join(vd,f"{vid}_characters.md");tf=os.path.join(vd,f"{vid}_text.md");sf=os.path.join(vd,f"{vid}_summary.md")
r("人设",os.path.exists(cf),[f"角色卡不存在"]if not os.path.exists(cf)else[])
tl=os.path.join(a.project_dir,"global_timeline.md");ti=[]
if os.path.exists(tl):
    with open(tl)as f:
        if vid not in f.read():ti.append(f"时间轴无{vid}")
r("时间",len(ti)==0,ti)
pi=[]
if os.path.exists(cf):
    with open(cf)as f:
        if"当前战力等级"not in f.read()and"本源战力上限"not in f.read():pi.append("缺战力")
r("战力",len(pi)==0,pi)
vm=re.search(r"Volume_(\d+)",vid);ii=[]
if vm and int(vm.group(1))>1 and os.path.exists(cf):
    with open(cf)as f:
        if"【过往经历汇总】"not in f.read():ii.append("缺继承")
r("继承",len(ii)==0,ii)
fi=[]
if os.path.exists(sf):
    with open(sf)as f:
        c=f.read()
    if"本卷新增伏笔"not in c or"本卷回收伏笔"not in c:fi.append("缺伏笔")
r("伏笔",len(fi)==0,fi)
ft=[]
if os.path.exists(tf):
    with open(tf)as f:
        for i,l in enumerate(f,1):
            if re.match(r"^第\d+章\s",l.strip()):ft.append(f"L{i}:第X章→第X话:{l.strip()}")
r("格式",len(ft)==0,ft)
si=[]
for r,_,fs in os.walk(vd):
    for fn in fs:
        if fn.endswith(".md"):
            try:open(os.path.join(r,fn),encoding="utf-8").read()
            except:si.append(f"非UTF-8:{fn}")
r("检索",len(si)==0,si)
vt=dt(vd);wmin,wmax=VR.get(vt,(50000,100000));wi=[]
if os.path.exists(tf):
    with open(tf)as f:co=f.read()
    ra=re.sub(r"[#*_>`\[\]\(\)-]","",co);ra=re.sub(r"\s+","",ra);wc=len(ra);ratio=er(ra)
    chs=re.findall(r"##\s*第\d+话",co);cc=len(chs)
    ud=[]
    for i,s in enumerate(re.split(r"##\s*第\d+话",co)[1:],1):
        st=re.sub(r"[#*_>`\[\]\(\)-]","",s);st=re.sub(r"\s+","",st)
        if len(st)<CMIN:ud.append(f"第{i}话{len(st)}字")
    if ud:wi.append(f"字数不足:{','.join(ud)}")
    if ratio<0.7:wi.append(f"有效率{ratio:.1%}<70%")
    wi.append(f"{vt}|目标{wmin:,}-{wmax:,}|实际{wc:,}|{cc}话|有效率{ratio:.1%}")
    if wc<wmin:wi.append(f"缺口{(wmin-wc):,}")
    elif wc>wmax:wi.append(f"超出{(wc-wmax):,}")
else:wi.append("正文不存在")
r("字数",wc>=wmin and ratio>=0.7 if os.path.exists(tf)else False,wi,True)
print("✅"if ok else"❌");sys.exit(0 if ok else 1)
