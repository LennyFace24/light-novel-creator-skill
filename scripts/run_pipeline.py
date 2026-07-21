#!/usr/bin/env python3
import argparse,os,subprocess,sys
S={"validate":("验证",lambda pd,vn:_run(pd,vn,"validate_volume.py",["--volume",vn])),"check":("校验",lambda pd,vn:_run(pd,vn,"check_consistency.py",[vn])),"wordcount":("字数",lambda pd,vn:_wc(pd,vn)),"init":("初始化",lambda pd,_:_run(pd,"","init_novel.py",[pd]))}
def _run(pd,vn,s,ex):
    sp=os.path.join(os.path.dirname(__file__),s);r=subprocess.run([sys.executable,sp,pd]+ex,capture_output=True,text=True);print(r.stdout)
    if r.returncode!=0:raise RuntimeError(r.stderr or f"{s}失败")
def _wc(pd,vn):
    import re;tf=os.path.join(pd,vn,f"{vn[:9]}_text.md")
    if not os.path.exists(tf):print("⚠️");return
    with open(tf)as f:c=f.read();t=re.sub(r"[#*_>`\[\]\(\)-]","",c);t=re.sub(r"\s+","",t);ch=len(re.findall(r"##\s*第\d+话",c))
    print(f"总:{len(t):,}字|{ch}话|均:{len(t)//max(ch,1):,}/话")
p=argparse.ArgumentParser();p.add_argument("project_dir");p.add_argument("volume",nargs="?",default="");p.add_argument("--stages",nargs="+",default=["validate","wordcount"],choices=list(S.keys()))
a=p.parse_args();print(f"📚|{a.volume or ''}|{'→'.join(a.stages)}")
for st in a.stages:
    n,f=S[st];print(f"\n▶{n}")
    try:f(a.project_dir,a.volume);print("✅")
    except Exception as e:print(f"❌{e}");sys.exit(1)
print("\n✅")
