# Bing 每日一图收集器

一个自动抓取 Bing 每日一图并通过网页展示的项目，使用 GitHub Actions 定时更新。

## ✨ 功能特色

- 🤖 **自动化更新** - 每天自动抓取 Bing 最新背景图片
- 🌍 **全球图片** - 来自全球各地的精美风景照
- 📱 **响应式设计** - 完美支持桌面和移动设备
- 💾 **本地缓存** - JSON 格式存储，便于后续使用
- 🎨 **美观界面** - 现代化卡片设计，提供良好用户体验

## 📋 项目结构

```
Blog/
├── .github/
│   └── workflows/
│       └── bing-wallpaper.yml      # GitHub Actions 工作流配置
├── scripts/
│   └── fetch_bing_wallpaper.py     # 抓取 Bing 图片的 Python 脚本
├── data/
│   └── wallpaper.json              # 存储图片数据（自动生成）
├── index.html                       # 网页展示页面
└── README.md                        # 项目说明文档
```

## 🚀 快速开始

### 前置要求

- GitHub 账户和仓库
- Python 3.10+ (本地测试时需要)
- 互联网连接

### 安装步骤

1. **克隆或创建仓库**
   ```bash
   git clone <your-repo-url>
   cd Blog
   ```

2. **启用 GitHub Pages** (可选，用于网页展示)
   - 在 GitHub 仓库设置中找到 `Pages` 选项
   - 选择 `Deploy from branch`
   - 选择 `main` 分支，根目录为 `/`
   - 保存设置

3. **验证工作流**
   - GitHub Actions 会自动运行
   - 检查 `Actions` 选项卡查看运行状态

### 本地测试

1. **安装依赖**
   ```bash
   pip install requests
   ```

2. **运行脚本**
   ```bash
   python scripts/fetch_bing_wallpaper.py
   ```

3. **查看结果**
   - 打开 `data/wallpaper.json` 查看数据
   - 在浏览器中打开 `index.html` 查看效果

## ⚙️ GitHub Actions 配置

### 自动更新计划

- **触发时间**: 每天 UTC 0:00（北京时间 08:00）
- **手动触发**: 支持在 GitHub Actions 页面手动执行

### 工作流详解

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # 每天 UTC 0:00
  workflow_dispatch:      # 支持手动触发
```

修改时间配置：
- `'0 0 * * *'` - 每天 UTC 0:00
- `'0 8 * * *'` - 每天 UTC 8:00（北京时间 16:00）
- `'0 */6 * * *'` - 每 6 小时一次

## 📊 数据格式

`data/wallpaper.json` 包含以下信息：

```json
[
  {
    "title": "图片标题",
    "description": "图片描述和版权信息",
    "image_url": "https://www.bing.com/...",
    "hd_url": "https://www.bing.com/... (高清版)",
    "date": "20240308",
    "fetch_time": "2024-03-08T10:00:00.000000"
  }
]
```

## 🌐 网页功能

- **图片展示**: 使用卡片布局展示每张图片
- **查看**: 点击"查看"按钮打开完整分辨率图片
- **下载**: 点击"下载"按钮直接下载高清背景图
- **刷新**: 手动刷新数据（重新加载 JSON）
- **自适应**: 自动适配各种屏幕尺寸

## 🔧 自定义配置

### 修改更新频率

编辑 `.github/workflows/bing-wallpaper.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # 修改这行
```

### 修改截图数量

编辑 `scripts/fetch_bing_wallpaper.py`:

```python
url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=zh-CN"
#                                                                    ↑
#                                                  修改 n=8 参数设置数量
```

### 更改地区

支持的地区代码：
- `zh-CN` - 中国
- `en-US` - 美国
- `ja-JP` - 日本
- `de-DE` - 德国

## 📝 常见问题

**Q: 为什么没有看到更新？**
- A: GitHub Actions 可能需要 5-10 分钟才能执行。检查 Actions 标签页查看运行状态。

**Q: 如何手动更新图片？**
- A: 可以在仓库的 Actions 标签页，找到 "Fetch Bing Daily Wallpaper" 工作流，点击"Run workflow"手动执行。

**Q: 可以自动更频繁地更新吗？**
- A: 可以。编辑 `.github/workflows/bing-wallpaper.yml` 的 `cron` 表达式，比如改为 `'0 */6 * * *'` 每 6 小时更新一次。

**Q: 网页无法访问图片怎么办？**
- A: 这是因为 Bing CDN 可能的访问限制。尝试：
  1. 直接访问 Bing 图片 URL
  2. 检查你的网络连接
  3. 使用 VPN 如果地区有限制

## 📄 许可证

MIT License - 可自由使用和修改

## 🙏 致谢

- 图片来源：[Microsoft Bing](https://www.bing.com)
- 基于 Bing Daily Wallpaper API

## 💡 改进建议

欢迎提交 Issue 和 Pull Request！

可能的改进方向：
- [ ] 添加图片搜索功能
- [ ] 收藏夹功能
- [ ] 暗色模式
- [ ] 多语言支持
- [ ] 图片详情信息（拍摄地点、相机等）
