# Bing每日一图 Collection

这是一个自动抓取Bing每日一图并展示的项目。

## 🎯 功能

- ✅ 每天自动抓取Bing每日一图
- ✅ 保留最近180天的图片
- ✅ 精美的响应式网页展示
- ✅ GitHub Pages 支持

## 📁 项目结构

```
.
├── .github/
│   └── workflows/
│       └── fetch-bing-image.yml    # GitHub Actions 工作流
├── scripts/
│   └── fetch_bing_image.py         # Python 抓取脚本
├── data/
│   └── bing-images.json            # 存储的图片数据
├── index.html                       # 前端展示页面
└── README.md                        # 本文件
```

## 🚀 使用方法

### 第一步：Fork 或 Clone 本仓库

```bash
git clone https://github.com/YOUR_USERNAME/bing-daily-image.git
cd bing-daily-image
```

### 第二步：启用 GitHub Actions

1. 进入你的仓库
2. 点击 `Settings` > `Actions` > `General`
3. 确保 `Actions permissions` 设置为 `Allow all actions and reusable workflows`
4. 确保 `Workflow permissions` 中 `Read and write permissions` 已勾选

### 第三步：启用 GitHub Pages

1. 在仓库设置中找到 `Pages`
2. 在 `Source` 中选择 `Deploy from a branch`
3. 选择 `main` 分支和 `/ (root)` 目录
4. 点击 Save

### 第四步：手动运行工作流（可选）

在 `Actions` 标签中选择 `fetch Bing Daily Image` 工作流，点击 `Run workflow` 手动触发一次。

## 📅 自动运行

工作流默认设置为每天 UTC 0:00 (北京时间 08:00) 自动运行。

## 🔍 API 说明

使用的是 Bing 官方的图片存档 API：
```
https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN
```

参数说明：
- `idx`: 图片索引，0 为今天，-1 为昨天，以此类推
- `n`: 返回数量
- `mkt`: 市场区域，zh-CN 为简体中文

## 💡 自定义

### 修改运行时间

编辑 `.github/workflows/fetch-bing-image.yml` 文件中的 cron 表达式：

```yaml
schedule:
  - cron: '0 0 * * *'  # 改为你想要的时间
```

[Cron 表达式参考](https://en.wikipedia.org/wiki/Cron)

### 修改保留天数

编辑 `scripts/fetch_bing_image.py` 中的 `max_days` 变量：

```python
max_days = 180  # 修改为你想要的天数
```

## 🛠️ 本地运行

需要 Python 3.10+

```bash
# 安装依赖
pip install requests

# 运行脚本
python scripts/fetch_bing_image.py
```

## 📝 数据格式

`data/bing-images.json` 中的数据格式：

```json
[
  {
    "url": "https://www.bing.com/th?id=OHR.xxx",
    "title": "图片标题",
    "copyright": "©图片版权信息",
    "date": "2024-01-15",
    "link": "https://www.bing.com/search?..."
  }
]
```

## 📄 License

MIT License

## 🙏 致谢

感谢 Bing 提供的精美壁纸。

---

创建于 2026年3月8日
