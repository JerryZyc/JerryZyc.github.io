# Robot Learning Notes (GitHub Pages)

This repository hosts a Jekyll-based personal site for robotics and robot learning notes, paper summaries, skills maps, and project retrospectives. It is compatible with GitHub Pages using the Minimal Mistakes theme.

## Quick Start

### Prerequisites

Install Ruby + Bundler.

- macOS: `brew install ruby`
- Ubuntu/WSL: `sudo apt-get install ruby-full build-essential zlib1g-dev`
- Windows (WSL recommended): use Ubuntu steps above.

Then install Bundler:

```
gem install bundler
```

### Run Locally

```
bundle install
bundle exec jekyll serve
```

Then open: `http://127.0.0.1:4000`

## Write a New Post

1. Copy a template from `notes/templates/`.
2. Save it into `_posts/` with name `YYYY-MM-DD-title.md`.
3. Update front matter: `title`, `date`, `categories`, `tags`.
4. Write content in Markdown.

Example file name:

```
2026-02-01-paper-some-title.md
```

## Publish to GitHub Pages

1. Ensure repo name is `<username>.github.io`.
2. Push to `main` branch.
3. GitHub Pages will build and deploy automatically.

## Notes

- Customize `_config.yml` with your name, avatar, and URLs.
- Put images under `assets/images`.
- Use `/search/` for site search, `/tags/` for tags, `/categories/` for categories.
