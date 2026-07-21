# /novel-persistence-skill

适配轻小说。核心：持久化架构 + 字数管控 + 三级大纲(含修改权限) + 强制串行 + 有效增量检测 + 大纲扩容3优先级。

**最优先级**：扩写=新增事件。描写>30%无效。有效增量<70%重做。大纲可为增量让路。未达标不启下话。

`/novel-persistence-skill` → init / preload / write / outline / archive / validate / wordcount-rescue / character / foreshadow / next-volume
