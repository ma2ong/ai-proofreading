#!/usr/bin/env python3
"""
图片上传到图床脚本
支持sm.ms、imgur等常见图床

使用方法：
    python scripts/upload_image.py <图片路径>
    python scripts/upload_image.py <图片路径> --批量
    python scripts/upload_image.py --batch <目录路径>
"""

import os
import sys
import json
import argparse
from pathlib import Path

# 图床配置（可以根据需要修改）
IMAGE_HOSTS = {
    "smms": {
        "api_url": "https://sm.ms/api/v2/upload",
        "header": "Authorization",
        # 需要配置API Key
    },
    "imgur": {
        "api_url": "https://api.imgur.com/3/image",
        "header": "Authorization",
        # 需要配置Client ID
    }
}

def upload_to_smms(image_path, api_key=None):
    """上传到SM.MS图床"""
    import requests

    if api_key is None:
        api_key = os.environ.get("SMMS_API_KEY", "")

    url = "https://sm.ms/api/v2/upload"
    headers = {"Authorization": api_key} if api_key else {}

    with open(image_path, "rb") as f:
        files = {"smfile": f}
        response = requests.post(url, files=files, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            return data.get("data", {}).get("url")
        else:
            # 检查是否因为重复上传
            if "image exists" in str(data).lower():
                return data.get("data", {}).get("url")
            raise Exception(f"Upload failed: {data}")
    else:
        raise Exception(f"HTTP Error: {response.status_code}")


def upload_to_imgur(image_path, client_id=None):
    """上传到Imgur图床"""
    import requests

    if client_id is None:
        client_id = os.environ.get("IMGUR_CLIENT_ID", "")

    url = "https://api.imgur.com/3/image"
    headers = {"Authorization": f"Client-ID {client_id}"}

    with open(image_path, "rb") as f:
        import base64
        image_data = base64.b64encode(f.read()).decode("utf-8")
        payload = {"image": image_data}
        response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("link")
    else:
        raise Exception(f"Imgur upload failed: {response.text}")


def upload_image(image_path, host="auto"):
    """
    上传图片到图床

    Args:
        image_path: 图片路径
        host: 图床类型 ("smms", "imgur", "auto")

    Returns:
        str: 图片URL
    """
    image_path = Path(image_path)
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    print(f"📤 Uploading: {image_path.name}")

    try:
        # 尝试多个图床
        if host in ["auto", "smms"]:
            try:
                url = upload_to_smms(str(image_path))
                if url:
                    print(f"✅ Success (SM.MS): {url}")
                    return url
            except Exception as e:
                print(f"⚠️ SM.MS failed: {e}")

        if host in ["auto", "imgur"]:
            try:
                url = upload_to_imgur(str(image_path))
                if url:
                    print(f"✅ Success (Imgur): {url}")
                    return url
            except Exception as e:
                print(f"⚠️ Imgur failed: {e}")

        raise Exception("All hosts failed")

    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return None


def generate_markdown_link(image_url, description=""):
    """生成Markdown格式的图片链接"""
    if description:
        return f"![{description}]({image_url})"
    return f"![]({image_url})"


def batch_upload(image_dir, host="auto"):
    """批量上传目录下的所有图片"""
    image_dir = Path(image_dir)
    if not image_dir.exists():
        raise FileNotFoundError(f"Directory not found: {image_dir}")

    # 支持的图片格式
    extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

    images = [f for f in image_dir.iterdir() if f.suffix.lower() in extensions]

    if not images:
        print(f"⚠️ No images found in {image_dir}")
        return []

    results = []
    for image_path in sorted(images):
        url = upload_image(str(image_path), host)
        if url:
            md_link = generate_markdown_link(url, image_path.stem)
            results.append({
                "filename": image_path.name,
                "url": url,
                "markdown": md_link
            })

    return results


def main():
    parser = argparse.ArgumentParser(description="图片上传到图床")
    parser.add_argument("path", nargs="?", help="图片路径或目录路径")
    parser.add_argument("--batch", "-b", action="store_true", help="批量模式（上传目录下所有图片）")
    parser.add_argument("--host", "-h", default="auto",
                        choices=["auto", "smms", "imgur"],
                        help="图床类型")
    parser.add_argument("--output", "-o", help="输出JSON文件路径")

    args = parser.parse_args()

    if not args.path:
        parser.print_help()
        print("\n💡 示例:")
        print("  python scripts/upload_image.py photo.png")
        print("  python scripts/upload_image.py --batch ./images/")
        return

    try:
        if args.batch or os.path.isdir(args.path):
            results = batch_upload(args.path, args.host)
            print(f"\n📊 批量上传完成: {len(results)}/{len(list(Path(args.path).iterdir())) if os.path.isdir(args.path) else 0}")

            # 输出Markdown格式
            print("\n--- Markdown 链接 ---")
            for r in results:
                print(r["markdown"])

            # 保存JSON结果
            if args.output:
                with open(args.output, "w", encoding="utf-8") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                print(f"\n💾 结果已保存到: {args.output}")

        else:
            url = upload_image(args.path, args.host)
            if url:
                md_link = generate_markdown_link(url)
                print(f"\n📤 Markdown 格式:")
                print(md_link)

                # 保存到剪贴板（如果可用）
                try:
                    import pyperclip
                    pyperclip.copy(md_link)
                    print("📋 已复制到剪贴板")
                except ImportError:
                    pass

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
