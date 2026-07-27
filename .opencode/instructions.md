# opencode 操作指南

## 1. 本地开发环境搭建

### 1.1 必要软件

| 软件 | 安装方式 | 用途 |
|------|----------|------|
| **Ruby 3.4+** | `winget install "Ruby 3.4 with MSYS2"` | Jekyll 构建核心 |
| **Bundler** | 随 Ruby 自带，`gem install bundler` | Ruby 依赖管理 |
| **Python 3.x** | `winget install Python.Python.3.12` | 本地 HTTP 预览服务器 |
| **Git** | `winget install Git.Git` | 版本控制 |
| **VS Code** | `winget install Microsoft.VisualStudioCode` | 代码编辑 |

### 1.2 Gem 镜像配置（国内网络优化）

```powershell
# bundler 配置使用清华镜像
bundle config mirror.https://rubygems.org/ https://mirrors.tuna.tsinghua.edu.cn/rubygems
```

### 1.3 安装依赖

```powershell
# 首次安装
bundle install

# 构建站点
bundle exec jekyll build

# 实时预览（含自动重建）
bundle exec jekyll serve
```

### 1.4 常见问题

- **SSL 证书错误**：gem 镜像不可用，切换到清华源 `mirrors.tuna.tsinghua.edu.cn/rubygems`
- **Bundler 版本冲突**：删除 `Gemfile.lock` 后重新 `bundle install`
- **远程主题下载失败**：已切换到本地 gem 主题 `minimal-mistakes-jekyll`，无需网络

## 2. 服务器本地可视化检测

### 2.1 启动 HTTP 预览

```powershell
# Jekyll 实时预览（推荐，含自动重建）
bundle exec jekyll serve

# 或使用 Python HTTP 服务器（仅静态文件）
Start-Process python -ArgumentList "-m", "http.server", "4000" -WorkingDirectory "_site"
Start-Process "http://localhost:4000"
```

### 2.2 检测与调试

```powershell
# 检测端口是否在监听
netstat -ano | Select-String ":4000" | Select-String "LISTENING"

# 测试 HTTP 响应
try { $wc = New-Object System.Net.WebClient; $response = $wc.DownloadString("http://localhost:4000"); Write-Output "OK - $($response.Length) chars" } catch { Write-Output "Error: $_" }

# 清理端口（服务器异常时）
Get-Process -Id (Get-NetTCPConnection -LocalPort 4000 -ErrorAction SilentlyContinue).OwningProcess | Stop-Process -Force
```

### 2.3 构建后预览

```powershell
# Kill 旧进程
Get-Process -Id (Get-NetTCPConnection -LocalPort 4000 -ErrorAction SilentlyContinue).OwningProcess -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue

# 构建
bundle exec jekyll build

# 启动预览
Start-Process python -ArgumentList "-m", "http.server", "4000" -WorkingDirectory "_site"
Start-Process "http://localhost:4000"
```

## 3. AI 聊天服务

项目内置 RAG 聊天助手，基于全站内容检索 + DeepSeek API。

### 3.1 启动服务

```powershell
# 设置 API Key 并启动
$env:DEEPSEEK_API_KEY = "sk-your-key"
python server/main.py
```

服务默认运行在 `http://localhost:5000`，前端聊天窗自动连接。

### 3.2 重建索引

当新增/修改文章后，需重建检索索引：

```powershell
python server/indexer.py
```

### 3.3 完整启动流程

```powershell
# 1. 构建 Jekyll 站点
bundle exec jekyll build

# 2. 启动 AI 聊天服务（后台）
$env:DEEPSEEK_API_KEY = "sk-your-key"
Start-Process python -ArgumentList "server/main.py" -WorkingDirectory "."

# 3. 启动 HTTP 预览（后台）
Start-Process python -ArgumentList "-m", "http.server", "4000" -WorkingDirectory "_site"

# 4. 打开浏览器
Start-Process "http://localhost:4000"
```

### 3.4 文件说明

| 文件 | 说明 |
|------|------|
| `server/main.py` | FastAPI 服务端（检索 + DeepSeek API） |
| `server/indexer.py` | TF-IDF 索引构建器 |
| `server/requirements.txt` | Python 依赖（轻量，无 PyTorch） |
| `assets/js/chat-widget.js` | 悬浮聊天窗（右下角） |
| `assets/css/chat-widget.css` | 聊天窗样式（适配暗色主题） |
| `.opencode/chroma_db/` | 索引存储目录（向量 + 元数据） |

## 4. 项目概览

本项目是 Jerry Zhu（JerryZyc）的个人主页与技术博客，基于 **Jekyll + GitHub Pages** 构建，使用 **Minimal Mistakes** 主题（dark skin）。

### 核心内容

| 板块 | 说明 |
|------|------|
| `_posts/` | 博客文章，4 个分类：`learning`（学习笔记）、`paper`（论文阅读）、`skills`（技能）、`work`（项目复盘） |
| `_pages/` | 独立页面：关于、分类页、标签页、搜索、知识图谱索引等 |
| `learning/` | 知识图谱目录树，~60+ 个知识节点文件，按 ML/DL/RL/交叉概念 组织 |
| `skills/` | 9 个 AI 辅助技能定义（SKILL.md），用于内容生成、质量检查等 |
| `notes/` | 草稿与模板 |
| `assets/` | 自定义 SASS 样式、图片、论文 PDF |
| `_data/navigation.yml` | 主导航栏（7 项） |
| `_includes/head/custom.html` | MathJax 3 + 聊天窗 widget |
| `server/` | Python FastAPI 聊天服务端（RAG + DeepSeek API） |
| `assets/js/chat-widget.js` | 前端悬浮聊天窗脚本 |
| `assets/css/chat-widget.css` | 聊天窗样式 |

### 技术栈

- Jekyll 3.10 + `github-pages` gem
- 本地主题 `minimal-mistakes-jekyll` 4.28（dark skin）
- kramdown (GFM) + MathJax 3（`$...$` 行内 / `$$...$$` 行间）
- Lunr.js 客户端搜索
- 自定义 CSS（`assets/css/main.scss`）：透明面板、backdrop blur、青绿色调

### 写作规范

见 `CONTRIBUTING.md`：
- 文件名：`YYYY-MM-DD-分类-英文短横.md`
- 必填 front matter：`title`, `date`, `categories`（限 `learning`/`paper`/`skills`/`work`）, `tags`
- 论文类额外字段：`paper.venue`, `paper.year`, `paper.authors`, `paper.pdf`, `status`
