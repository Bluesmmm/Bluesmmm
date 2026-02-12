# Bluesmmm GitHub Profile README - 部署指南

## 📋 概述

这是一个为 **Bluesmmm**（机器学习开发者）创建的 GitHub 个人主页 README 仓库。包含中英文双语版本，以及通过 GitHub Actions 自动更新的 ML/Python 名言。

---

[English](#english) | [简体中文](#简体中文)

---

<a name="english"></a>
## English Version

### Quick Start

#### 1. Create the GitHub Repository

1. Create a **new repository** on GitHub named exactly `Bluesmmm` (must match your username)
2. **Do NOT** initialize with README (we already have one)
3. Upload all files from this directory to the repository

#### 2. Push to GitHub

```bash
cd Bluesmmm
git init
git add .
git commit -m "Initial commit: GitHub Profile README (Bilingual)"
git branch -M main
git remote add origin https://github.com/Bluesmmm/Bluesmmm.git
git push -u origin main
```

#### 3. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click on **Actions** tab
3. Click **I understand my workflows, go ahead and enable them** (if prompted)
4. Go to **Update README with ML Quotes (Bilingual)** workflow
5. Click **Run workflow** → **Run workflow** to trigger manually

### File Structure

```
Bluesmmm/
├── README.template.md          # Chinese template - edit this
├── README_EN.template.md       # English template - edit this
├── README.md                   # Auto-generated Chinese version
├── README_EN.md                # Auto-generated English version
├── scripts/
│   └── update_readme.py        # Python script for dynamic content
├── .github/
│   └── workflows/
│       └── update-readme.yml   # GitHub Actions workflow
└── SETUP.md                    # This file
```

### Customization

**Edit Static Content**: Always edit `README.template.md` (Chinese) or `README_EN.template.md` (English) - **never** the generated files directly.

**Add More Quotes**: Edit `scripts/update_readme.py` and add to the quote lists:
- `ML_QUOTES_EN` for English quotes
- `ML_QUOTES_CN` for Chinese quotes

**Change Theme**: Replace `theme=radical` with other themes like `dark`, `gotham`, `blue_green`, `dracula`.

---

<a name="简体中文"></a>
## 简体中文版本

### 快速开始

#### 1. 创建 GitHub 仓库

1. 在 GitHub 上创建一个名为 **`Bluesmmm`** 的新仓库（必须与用户名完全一致）
2. **不要**初始化 README（我们已经有了）
3. 将此目录中的所有文件上传到仓库

#### 2. 推送到 GitHub

```bash
cd Bluesmmm
git init
git add .
git commit -m "Initial commit: GitHub Profile README (Bilingual)"
git branch -M main
git remote add origin https://github.com/Bluesmmm/Bluesmmm.git
git push -u origin main
```

#### 3. 启用 GitHub Actions

1. 进入 GitHub 上的仓库
2. 点击 **Actions** 标签
3. 点击 **我明白我的工作流，继续启用**（如果出现提示）
4. 进入 **Update README with ML Quotes (Bilingual)** 工作流
5. 点击 **Run workflow** → **Run workflow** 手动触发

### 文件结构

```
Bluesmmm/
├── README.template.md          # 中文模板 - 编辑此文件
├── README_EN.template.md       # 英文模板 - 编辑此文件
├── README.md                   # 自动生成的中文版
├── README_EN.md                # 自动生成的英文版
├── scripts/
│   └── update_readme.py        # 动态内容生成脚本
├── .github/
│   └── workflows/
│       └── update-readme.yml   # GitHub Actions 工作流
└── SETUP.md                    # 本文件
```

### 自定义

**编辑静态内容**：始终编辑 `README.template.md`（中文）或 `README_EN.template.md`（英文）—— **切勿**直接编辑生成的文件。

**添加更多名言**：编辑 `scripts/update_readme.py` 并添加到名言列表：
- `ML_QUOTES_EN` 为英文名言
- `ML_QUOTES_CN` 为中文名言

**更改主题**：将 `theme=radical` 替换为其他主题，如 `dark`、`gotham`、`blue_green`、`dracula`。

### 工作流触发

工作流会在以下情况自动运行：
- **每小时一次**（通过 cron 定时）
- 当你**手动触发**时
- 当模板文件或脚本发生变化时

### 🌐 语言切换

访问者可以通过顶部的语言切换按钮在中英文版本之间切换：
- **README.md** - 中文版（默认主页）
- **README_EN.md** - 英文版

---

## 📊 动态服务使用

| 服务 | 用途 |
|---------|------|
| [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) | 统计卡片 |
| [shields.io](https://shields.io/) | 技术栈徽章 |
| [github-profile-trophy](https://github.com/ryo-ma/github-profile-trophy) | 成就展示 |
| [github-readme-streak-stats](https://github.com/Ashutosh00710/github-readme-streak-stats) | 贡献连续记录 |
| [badges.pufler.dev](https://badges.pufler.dev/) | 访客计数器 |

---

## 🎯 下一步

1. ✅ 个人主页 README 创建完成
2. ⏳ 向 GitHub 添加实际项目
3. ⏳ 获取 Stars 和贡献，统计数据才会显示
4. ⏳ （可选）添加博客并配置 RSS 订阅
