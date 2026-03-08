@echo off
REM Windows 本地测试脚本

echo ===================================
echo Bing 每日一图 - 本地测试
echo ===================================
echo.

REM 检查 Python 版本
echo 📋 检查 Python 版本...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 Python，请先安装
    exit /b 1
)

python --version
echo.

REM 检查依赖
echo 📋 检查依赖...
python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 requests，正在安装...
    pip install requests
) else (
    echo ✅ requests 已安装
)

python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 pillow，正在安装...
    pip install pillow
) else (
    echo ✅ pillow 已安装
)
echo.

REM 运行脚本
echo 🚀 运行脚本...
echo ---
python scripts/fetch_bing_image.py
echo ---
echo.

REM 检查输出
if exist "data\bing-images.json" (
    echo ✅ 文件已生成: data\bing-images.json
    echo.
    echo 📊 数据内容预览:
    python -m json.tool data\bing-images.json | findstr /n "^" | findstr /m "^[1-9][0-9]*:" || type data\bing-images.json
    echo.
    echo ✅ 测试成功！
) else (
    echo ❌ 文件生成失败
    exit /b 1
)
