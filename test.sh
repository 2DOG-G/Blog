#!/bin/bash
# 本地测试脚本

echo "==================================="
echo "Bing 每日一图 - 本地测试"
echo "==================================="
echo ""

# 检查 Python 版本
echo "📋 检查 Python 版本..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到 Python 3，请先安装"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python 版本: $PYTHON_VERSION"
echo ""

# 检查依赖
echo "📋 检查依赖..."
if python3 -c "import requests" 2>/dev/null; then
    echo "✅ requests 已安装"
else
    echo "❌ 未找到 requests，正在安装..."
    pip install requests
fi

if python3 -c "import PIL" 2>/dev/null; then
    echo "✅ pillow 已安装"
else
    echo "❌ 未找到 pillow，正在安装..."
    pip install pillow
fi
echo ""

# 运行脚本
echo "🚀 运行脚本..."
echo "---"
python3 scripts/fetch_bing_image.py
echo "---"
echo ""

# 检查输出
if [ -f "data/bing-images.json" ]; then
    echo "✅ 文件已生成: data/bing-images.json"
    echo ""
    echo "📊 数据内容预览:"
    python3 -m json.tool data/bing-images.json | head -20
    echo ""
    echo "✅ 测试成功！"
else
    echo "❌ 文件生成失败"
    exit 1
fi
