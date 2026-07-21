#!/usr/bin/env python3
import argparse,os,shutil
T=os.path.join(os.path.dirname(__file__),"..","assets","templates")
GF=["global_characters.md","global_timeline.md","global_foreshadowing.md","global_story_outline.md"]
VF=["Volume_XX_text.md","Volume_XX_characters.md","Volume_XX_summary.md"]
VT={"opening":("开篇首卷",60000,90000,12),"main":("主线正篇卷",65000,85000,12),"daily":("日常过渡卷",50000,70000,10),"climax":("高潮决战卷",80000,100000,14)}
p=argparse.ArgumentParser();p.add_argument("project_dir");p.add_argument("--volume-name",default="第一卷");p.add_argument("--volume-type",choices=list(VT.keys()),default="opening");p.add_argument("--total-words",type=int,default=0)
a=p.parse_args()
if not os.path.isdir(a.project_dir):print(f"❌ {a.project_dir}");exit(1)
n,wmin,wmax,ch=VT[a.volume_type]
for f in GF:
    d=os.path.join(a.project_dir,f)
    if not os.path.exists(d):shutil.copy2(os.path.join(T,f),d);print(f"✅ {f}")
vd=f"Volume_01_{a.volume_name}";os.makedirs(os.path.join(a.project_dir,vd),exist_ok=True)
for f in VF:
    d=os.path.join(a.project_dir,vd,f.replace("Volume_XX","Volume_01"))
    if not os.path.exists(d):shutil.copy2(os.path.join(T,f),d)
open(os.path.join(a.project_dir,"字数分配表.md"),"w",encoding="utf-8").write(f"# 字数分配表\n\n卷:{n}\n字数:{wmin:,}-{wmax:,}\n话数:{ch}\n最小节拍:{ch*3}\n单话:~{wmax//ch:,}")
print("✅")
