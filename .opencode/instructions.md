# opencode 操作指南

## 1. 内容沉淀体系（我如何帮你整理知识）

你每天不定期发来的内容，我会按以下流程处理：

```
你发来材料 → 判断内容类型 → 提取核心知识 → 写入对应位置 → 更新索引
```

### 内容类型和对应位置

| 你发的内容 | 我会生成 | 存放位置 |
|-----------|---------|---------|
| 论文链接/PDF/笔记 | 论文笔记（标准模板） | `_posts/` + 论文 PDF → `assets/papers/` |
| 技术思考/心得 | 学习笔记（概念+实践要点） | `_posts/` |
| 工作项目复盘 | 项目复盘（背景-方案-教训） | `_posts/` |
| 行业新闻/动态 | 轻量笔记或更新现有知识节点 | `_posts/` 或更新 `learning/` |
| 知识碎片/灵感 | 先记入 `notes/raw.md`，成熟后提炼 | `notes/raw.md` → `_posts/` |

### 论文笔记模板（`notes/templates/paper-note-template.md`）

```yaml
---
title: "论文名"
date: YYYY-MM-DD
categories: [paper]
tags: [关键词]
status: reading  # to-read | reading | done | reproduced
paper:
  venue: "会议/期刊"
  year: YYYY
  authors: "作者"
  pdf: "/assets/papers/xxx.pdf"
---
```

### 学习笔记模板

```yaml
---
title: "概念名"
date: YYYY-MM-DD
categories: [learning]
tags: [关键词]
---
```

结构：定义 → 为什么重要 → 核心要点 → 常见误区 → 实践清单 → 关联知识

### 项目复盘模板（`notes/templates/work-project-template.md`）

```yaml
---
title: "项目名"
date: YYYY-MM-DD
categories: [work]
tags: [project, 关键词]
---
```

结构：背景 → 目标 → 方案 → 结果 → 经验教训 → 下一步行动

---

## 2. 本地开发环境搭建

### 2.1 必要软件

| 软件 | 安装方式 | 用途 |
|------|----------|------|
| **Ruby 3.4+** | `winget install "Ruby 3.4 with MSYS2"` | Jekyll 构建核心 |
| **Bundler** | 随 Ruby 自带 | Ruby 依赖管理 |
| **Python 3.x** | `winget install Python.Python.3.12` | 本地 HTTP 预览 + 聊天服务 |
| **Git** | `winget install Git.Git` | 版本控制 |
| **VS Code** | `winget install Microsoft.VisualStudioCode` | 代码编辑 |

### 2.2 Gem 镜像配置（国内网络优化）

```powershell
bundle config mirror.https://rubygems.org/ https://mirrors.tuna.tsinghua.edu.cn/rubygems
```

### 2.3 安装依赖

```powershell
bundle install
```

### 2.4 常见问题

- **SSL 证书错误**：gem 镜像不可用，切换到清华源
- **Bundler 版本冲突**：删除 `Gemfile.lock` 后重新 `bundle install`

---

## 3. 本地预览

```powershell
# 完整启动（构建 + 聊天服务 + 预览）
bundle exec jekyll build
python server/indexer.py   # 重建聊天索引
$env:DEEPSEEK_API_KEY = "sk-your-key"
Start-Process python -ArgumentList "server/main.py" -WorkingDirectory "."
Start-Process python -ArgumentList "-m", "http.server", "4000" -WorkingDirectory "_site"
Start-Process "http://localhost:4000"
```

---

## 4. 发布流程

```powershell
# 新增内容后
bundle exec jekyll build    # 验证构建成功
git add -A
git commit -m "type: 简述"
git push                    # GitHub Actions 自动部署
```

---

## 5. 知识图谱维护

`learning/` 目录是结构化的知识树，按 ML/DL/RL/交叉概念 组织。

- 新增概念时：在对应目录下创建 `.md` 文件
- 更新旧概念时：补充新理解、修正错误、添加关联
- 重构时：合并碎片节点、拆分过大的节点

---

## 6. 质量要求

- 每篇笔记必须有清晰的**核心论点**或**学习目标**
- 用**自己的话**写，不只是翻译或摘抄
- 关联已有知识（"参见 XXX"）
- 论文笔记必须有**批判性思考**（优点/局限/如何用于我的项目）
- 定期回顾 `status: draft` 的内容，补充完善
