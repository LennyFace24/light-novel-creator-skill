# light-novel-creator-skill 📚 v1.6

**长篇小说AI分卷创作·持久化规范执行技能**

[![GitHub](https://img.shields.io/badge/GitHub-light--novel--creator--skill-181717?logo=github)](https://github.com/LennyFace24/light-novel-creator-skill)

---

## 故事增量铁律（最优先级）

**扩写 = 新增独立故事事件。禁止任何形式的描写堆砌。**

| 规则 | 阈值 | 后果 |
|------|------|------|
| 修饰性描写占比 | > **30%** | 判定无效扩写 |
| 有效增量字数占比 | < **70%** | 续写无效，须重做 |

## 强制串行创作

**一话写完锁定再写下一话。当前话未达标，绝对禁止启动下一话。**

## 安装

```bash
git clone https://github.com/LennyFace24/light-novel-creator-skill.git ~/.claude/skills/novel-persistence-skill
# 或: cd novel-persistence-skill && chmod +x install.sh && ./install.sh
```

## 使用

`/novel-persistence-skill init | write | outline estimate|expand|plan | archive | validate | wordcount-rescue`

## 卷型

| 类型 | 字数 | 话数 |
|------|------|------|
| 开篇首卷 | 7-9万 | 10-14 |
| 主线正篇 | 6.5-8.5万 | 10-14 |
| 日常过渡 | 5-7万 | 8-12 |
| 高潮决战 | 8-10万 | 12-16 |

单话3500-6000。MIT
