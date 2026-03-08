# 常用配置参考

## Cron 表达式示例

### 基本格式
```
分 时 日 月 周几
0  0  *  *  *
```

### 常用配置

```yaml
# 每天北京时间 08:00 (UTC 0:00)
- cron: '0 0 * * *'

# 每天北京时间 12:00 (UTC 4:00)
- cron: '0 4 * * *'

# 每天北京时间 20:00 (UTC 12:00)
- cron: '0 12 * * *'

# 每 6 小时运行一次
- cron: '0 */6 * * *'

# 每 3 小时运行一次
- cron: '0 */3 * * *'

# 仅在周一运行
- cron: '0 0 * * 1'

# 每个月的第一天运行
- cron: '0 0 1 * *'

# 工作日每天 09:00 运行
- cron: '0 1 * * 1-5'

# 周末 10:00 运行
- cron: '0 2 * * 0,6'
```

## 地区代码参考

```python
# 在 fetch_bing_image.py 中修改:
"mkt": "zh-CN"

# 常用地区代码:
"mkt": "en-US"    # 美国
"mkt": "en-GB"    # 英国
"mkt": "zh-CN"    # 中国简体
"mkt": "zh-TW"    # 台湾繁体
"mkt": "ja-JP"    # 日本
"mkt": "ko-KR"    # 韩国
"mkt": "fr-FR"    # 法国
"mkt": "de-DE"    # 德国
"mkt": "es-ES"    # 西班牙
"mkt": "it-IT"    # 意大利
"mkt": "ru-RU"    # 俄罗斯
"mkt": "pt-BR"    # 巴西葡萄牙语
```

## Python 脚本参数说明

```python
# 在 fetch_bing_image.py 中修改:

# 最多保留的天数
max_days = 180          # 修改为需要的天数

# API 请求参数
params = {
    "format": "js",     # 返回格式(json)
    "idx": 0,           # 图片索引: 0=今天, 1=昨天, etc
    "n": 1,             # 返回数量
    "mkt": "zh-CN"      # 市场/语言代码
}

# 超时设置 (秒)
timeout = 10            # HTTP 请求超时
```

## GitHub Actions 权限配置

### 必须配置项

进入仓库 → Settings → Actions → General:

1. **Actions permissions**
   - ✅ Allow all actions and reusable workflows

2. **Workflow permissions**
   - ✅ Read and write permissions
   - ✅ Allow GitHub Actions to create and approve pull requests

### API Token (如需要)

如果需要调用其他 API:

1. 进入 Settings → Developer settings → Personal access tokens
2. 创建 token，赋予所需权限
3. 在 Settings → Secrets and variables → Actions 中添加
4. 在工作流中使用: `${{ secrets.YOUR_TOKEN_NAME }}`

## GitHub Pages 域名配置

### GitHub Pages 默认域名
```
https://YOUR_USERNAME.github.io/bing-daily-image
```

### 自定义域名 (可选)

1. 购买域名（如 example.com）
2. 在域名提供商处配置 DNS：
   - 添加 CNAME 记录: `YOUR_USERNAME.github.io`
   - 或添加 A 记录指向 GitHub IP
3. 在仓库 Settings → Pages → Custom domain 输入域名
4. 点击 Save，GitHub 会自动为你配置 HTTPS

## 高级定制

### 修改首页

编辑 `home.html` 自定义欢迎页面

### 修改样式

编辑 `index.html` 中的 `<style>` 部分自定义图片库样式

### 添加更多信息

在 `index.html` 中添加新的 HTML 元素和 JavaScript 功能

### 数据处理

如需处理图片数据，可在 Python 脚本中添加：
```python
# 在 save_images() 之前处理数据
# 例如: 下载图片、生成缩略图等
```

---

更多帮助请查看 [README.md](README.md) 和 [QUICKSTART.md](QUICKSTART.md)
