# /novel-persistence-skill

适配轻小说。核心：持久化架构 + 字数管控 + 三级大纲 + 锚点 + 强制续写 + **有效增量检测** + **强制串行创作** + **下一话锁定**。

**最优先级**：扩写=新增事件。描写>30%无效。有效增量<70%重做。**一话写完锁定再写下一话，未达标不启下话。**

`/novel-persistence-skill` → init / preload / write / outline / archive / validate / wordcount-rescue / character / foreshadow / next-volume
