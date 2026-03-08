#!/usr/bin/env python3
"""
抓取Bing每日一图的脚本
"""

import requests
import json
import os
from datetime import datetime

def fetch_bing_wallpaper():
    """从Bing API获取每日一图信息"""
    
    # Bing每日一图API (中国区) - 只获取当天图片
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # 提取图片信息
        wallpapers = []
        for image in data.get('images', []):
            url = image.get('url', '')
            # 生成4K/UHD版本的URL
            uhd_url = url.replace('_1080x1920', '_UHD').replace('_1920x1080', '_UHD')
            # Bing 4K URL格式: 使用更高分辨率
            image_4k_url = uhd_url if '_UHD' in uhd_url else url + '&w=3840&h=2160'
            
            wallpaper = {
                'title': image.get('title', ''),
                'description': image.get('copyright', ''),
                'image_url': f"https://www.bing.com{url}",
                'hd_url': f"https://www.bing.com{uhd_url}",
                '4k_url': f"https://www.bing.com{image_4k_url}",
                'date': image.get('startdate', ''),
                'fetch_time': datetime.now().isoformat()
            }
            wallpapers.append(wallpaper)
        
        # 确保数据目录存在
        data_dir = 'data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # 保存为JSON文件
        output_file = os.path.join(data_dir, 'wallpaper.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(wallpapers, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 成功获取当天Bing背景图片")
        print(f"✓ 数据已保存到 {output_file}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"✗ 获取Bing图片失败: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ 解析JSON失败: {e}")
        return False

if __name__ == "__main__":
    success = fetch_bing_wallpaper()
    exit(0 if success else 1)
