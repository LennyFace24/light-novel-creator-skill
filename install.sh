#!/usr/bin/env bash
set -euo pipefail
SKILL="novel-persistence-skill"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DRY=false;PLAT="";PD="${PROJECT_DIR:-$(pwd)}"
usage(){echo "用法: install.sh [--platform <n>] [--project-dir <p>] [--dry-run]";echo "平台: claude copilot cursor windsurf gemini cline roo-code all";}
inst(){echo "  → $1";[ "$DRY" = false ]&&{mkdir -p "$(dirname "$1")";cp -R "$DIR" "$1";echo "  ✅";};}
while[[$#-gt0]];do case "$1" in --platform)PLAT="$2";shift2;;--project-dir)PD="$2";shift2;;--dry-run)DRY=true;shift;;--help)usage;exit0;;*)echo "未知:$1";usage;exit1;;esac;done
echo "📦$SKILL"
if[-n"$PLAT"];then case "$PLAT" in claude)inst "$HOME/.claude/skills/$SKILL";;copilot)inst "$HOME/.copilot/skills/$SKILL";;cursor)inst "$PD/.cursor/skills/$SKILL";;windsurf)inst "$PD/.windsurf/rules/$SKILL";;gemini)inst "$HOME/.gemini/skills/$SKILL";;cline)inst "$HOME/.cline/skills/$SKILL";;roo-code)inst "$HOME/.roo/skills/$SKILL";;all)inst "$HOME/.claude/skills/$SKILL";inst "$HOME/.agents/skills/$SKILL";;*)echo "❌:$PLAT";exit1;;esac
else[ -d "$HOME/.claude" ]&&inst "$HOME/.claude/skills/$SKILL";inst "$HOME/.agents/skills/$SKILL";fi
echo "";echo "✅ /$SKILL init"
