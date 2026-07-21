#!/usr/bin/env python3
import argparse,os,sys
GF=["global_characters.md","global_timeline.md","global_foreshadowing.md","global_story_outline.md"]
p=argparse.ArgumentParser();p.add_argument("project_dir");p.add_argument("--volume")
a=p.parse_args()
if not os.path.isdir(a.project_dir):print("❌");sys.exit(1)
if a.volume:
    vd=os.path.join(a.project_dir,a.volume);ok=True
    if not os.path.isdir(vd):print("❌");sys.exit(1)
    for f in[f"{a.volume[:9]}_text.md",f"{a.volume[:9]}_characters.md",f"{a.volume[:9]}_summary.md"]:
        fp=os.path.join(vd,f);s=os.path.getsize(fp)if os.path.isfile(fp)else 0;print(f"{'✅'if s>0 else'❌'}{f}({s}B)")
        if not s:ok=False
    sys.exit(0 if ok else 1)
ok=True
for f in GF:
    fp=os.path.join(a.project_dir,f);s=os.path.getsize(fp)if os.path.isfile(fp)else 0;print(f"{'✅'if s>0 else'❌'}{f}({s}B)")
    if not s:ok=False
for d in sorted(x for x in os.listdir(a.project_dir)if os.path.isdir(os.path.join(a.project_dir,x))and x.startswith("Volume_")):
    for f in[f"{d[:9]}_text.md",f"{d[:9]}_characters.md",f"{d[:9]}_summary.md"]:
        fp=os.path.join(a.project_dir,d,f);s=os.path.getsize(fp)if os.path.isfile(fp)else 0;print(f"{'✅'if s>0 else'❌'}{d}/{f}({s}B)")
        if not s:ok=False
sys.exit(0 if ok else 1)
