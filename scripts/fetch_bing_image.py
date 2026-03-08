#!/usr/bin/env python3
"""
抓取Bing每日一图脚本
"""

import requests
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import base64

def get_bing_image(days_offset=0):
    """
    获取Bing每日一图
    days_offset: 0表示今天，-1表示昨天，以此类推
    """
    url = "https://www.bing.com/HPImageArchive.aspx"
    params = {
        "format": "js",
        "idx": days_offset,
        "n": 1,
        "mkt": "zh-CN"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("images"):
            image_info = data["images"][0]
            return {
                "url": "https://www.bing.com" + image_info.get("url", ""),
                "title": image_info.get("title", ""),
                "copyright": image_info.get("copyright", ""),
                "date": (datetime.now() + timedelta(days=days_offset)).strftime("%Y-%m-%d"),
                "link": image_info.get("copyrightlink", "")
            }
    except Exception as e:
        print(f"错误: 抓取Bing图片失败 - {e}")
        return None

def load_existing_images():
    """加载现有的图片数据"""
    data_dir = Path(__file__).parent.parent / "data"
    data_file = data_dir / "bing-images.json"
    
    if data_file.exists():
        with open(data_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_images(images):
    """保存图片数据"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)
    
    data_file = data_dir / "bing-images.json"
    
    # 按日期降序排序，最新的在前
    images.sort(key=lambda x: x["date"], reverse=True)
    
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(images, f, ensure_ascii=False, indent=2)
    
    print(f"已保存 {len(images)} 张图片")

def download_image(url, save_dir):
    """下载图片到本地"""
    try:
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()
        
        filename = url.split("/")[-1].split("?")[0]
        filepath = save_dir / filename
        
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        return filepath
    except Exception as e:
        print(f"下载图片失败: {e}")
        return None

def main():
    # 获取最新的Bing每日一图
    print("正在抓取Bing每日一图...")
    new_image = get_bing_image(0)
    
    if not new_image:
        print("抓取失败")
        return
    
    # 加载现有图片
    images = load_existing_images()
    
    # 检查是否已存在今天的图片
    today = datetime.now().strftime("%Y-%m-%d")
    if any(img["date"] == today for img in images):
        print(f"今天的图片已存在: {today}")
        return
    
    # 添加新图片
    images.append(new_image)
    
    # 只保留最近180天的图片
    max_days = 180
    cutoff_date = (datetime.now() - timedelta(days=max_days)).strftime("%Y-%m-%d")
    images = [img for img in images if img["date"] >= cutoff_date]
    
    # 保存数据
    save_images(images)
    
    print(f"成功抓取: {new_image['title']}")
    print(f"日期: {new_image['date']}")
    print(f"版权: {new_image['copyright']}")

if __name__ == "__main__":
    main()
