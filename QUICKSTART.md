# 快速开始指南 🚀

## 📋 项目概述

这是一个全自动的GitHub Actions项目，每天自动抓取Bing每日一图，并在网页上展示。

## ⚡ 快速设置 (5分钟)

### 1️⃣ 创建 GitHub 仓库

```bash
# 初始化本地仓库  
git init
git add .
git commit -m "初始化项目"
```

### 2️⃣ 推送到 GitHub

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bing-daily-image.git
git push -u origin main
```

### 3️⃣ 配置 Actions 权限

进入仓库 → Settings → Actions → General
- ✅ 勾选 "Allow all actions and reusable workflows"
- ✅ 选择 "Read and write permissions"

### 4️⃣ 启用 GitHub Pages

进入仓库 → Settings → Pages
- 选择 "Deploy from a branch"
- 分支: `main`, 目录: `/ (root)`
- 点击 Save

### 5️⃣ 手动触发工作流 (可选)

进入 Actions 标签 → "抓取Bing每日一图" → "Run workflow"

✅ **完成！** 你的网站将在 `https://YOUR_USERNAME.github.io/bing-daily-image` 上线

## 📱 项目特性

| 功能 | 描述 |
|-----|------|
| 🤖 自动抓取 | 每天 08:00 (北京时间) 自动运行 |
| 💾 数据保存 | 保留最近 180 天的图片 |
| 🎨 精美展示 | 响应式设计，适配所有设备 |
| 📱 实时预览 | 网页每 5 分钟自动刷新 |
| 🔧 易于定制 | 配置文件清晰，易于修改 |

## 🎯 文件说明

```
📦 项目根目录
├── .github/workflows/fetch-bing-image.yml
│   └── GitHub Actions 工作流配置，定义自动任务
│
├── scripts/fetch_bing_image.py
│   └── Python 爬虫脚本，负责抓取和保存图片数据
│
├── data/bing-images.json
│   └── 图片数据库，存储所有抓取的图片信息
│
├── index.html
│   └── 主页面，展示所有图片（推荐首先查看）
│
├── home.html
│   └── 欢迎页面，简单而优雅的首页
│
├── README.md
│   └── 详细的项目文档
│
├── QUICKSTART.md
│   └── 本文件，快速入门指南
│
└── .gitignore
    └── Git 忽略文件配置
```

## 🔧 自定义配置

### 修改运行时间

编辑 `.github/workflows/fetch-bing-image.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # 改为你需要的时间
  # 例如: '0 8 * * *' = 每天 UTC 8:00
  # 例如: '0 */6 * * *' = 每 6 小时一次
```

### 修改保留天数

编辑 `scripts/fetch_bing_image.py`:

```python
max_days = 180  # 改为需要的天数
```

### 修改地区/语言

编辑 `scripts/fetch_bing_image.py`:

```python
params = {
    "mkt": "zh-CN"  # 改为其他地区代码
    # en-US: 美国英文
    # ja-JP: 日本
    # fr-FR: 法国
    # 等等
}
```

## 🌐 访问你的网站

工作流运行后，你可以通过以下方式访问：

1. **GitHub Pages 官方链接**: `https://YOUR_USERNAME.github.io/bing-daily-image`
2. **仓库设置中的 Pages 链接**: 在 Settings → Pages 中找到

如果访问不到，检查：
- ✓ GitHub Pages 是否已启用
- ✓ 工作流是否成功运行 (检查 Actions 标签)
- ✓ 是否已有提交到 main 分支

## 📊 工作流状态

在仓库的 Actions 标签中查看：
- 🟢 绿色: 工作流运行成功
- 🔴 红色: 工作流运行失败
- 🟡 黄色: 工作流正在运行

## 🐛 常见问题

### Q: 为什么图片没有显示？
A: 检查是否运行过工作流，可手动触发一次：Actions → 选择工作流 → Run workflow

### Q: 多久更新一次？
A: 默认每天北京时间 08:00 更新一次，可在工作流文件中修改

### Q: 可以显示多少天的图片？
A: 默认保留 180 天，修改脚本中的 `max_days` 变量即可

### Q: 如何备份图片？
A: 所有数据都保存在 `data/bing-images.json` 中，定期下载备份即可

## 🔐 隐私说明

- 本项目仅抓取 Bing 官方提供的公开数据
- 所有数据存储在你自己的 GitHub 仓库中
- 不收集或传输任何个人信息

## 📝 许可证

MIT License - 自由使用和修改

## 💬 反馈和贡献

如有问题或改进建议，欢迎通过 Issues 反馈！

---

**祝你使用愉快！** 🎉
