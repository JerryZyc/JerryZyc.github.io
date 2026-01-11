# 机器人学习笔记（GitHub Pages）

此仓库是基于 Jekyll 的个人站点，用于记录机器人与机器人学习的学习笔记、论文摘要、技能图谱与项目复盘。使用 Minimal Mistakes 主题，兼容 GitHub Pages。

## 快速开始

### 前置条件

安装 Ruby 与 Bundler。

- macOS：`brew install ruby`
- Ubuntu/WSL：`sudo apt-get install ruby-full build-essential zlib1g-dev`
- Windows（推荐 WSL）：按 Ubuntu 步骤安装。

然后安装 Bundler：

```
gem install bundler
```

### 本地运行

```
bundle install
bundle exec jekyll serve
```

浏览：`http://127.0.0.1:4000`

## 新建文章

1. 从 `notes/templates/` 复制模板。
2. 保存到 `_posts/`，命名为 `YYYY-MM-DD-title.md`。
3. 更新 front matter：`title`、`date`、`categories`、`tags`。
4. 用 Markdown 撰写内容。

示例文件名：

```
2026-02-01-paper-some-title.md
```

## 发布到 GitHub Pages

1. 确保仓库名为 `<username>.github.io`。
2. 推送到 `main` 分支。
3. GitHub Pages 会自动构建并部署。

## 备注

- 在 `_config.yml` 中配置你的姓名、头像与链接。
- 图片放在 `assets/images`。
- `/search/` 搜索，`/tags/` 标签，`/categories/` 分类。
