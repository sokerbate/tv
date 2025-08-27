import json
import gzip
import base58
import urllib.parse
import sys
import os

def main():
    config_path = "config.json"

    # 检查文件是否存在
    if not os.path.exists(config_path):
        print(f"❌ Error: {config_path} not found")
        sys.exit(1)

    # 读取 JSON
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format in {config_path}")
        print(e)
        sys.exit(1)

    # 转成字符串
    config_str = json.dumps(config_data, separators=(",", ":"), ensure_ascii=False)

    # 压缩
    compressed = gzip.compress(config_str.encode("utf-8"))

    # Base58 编码
    encoded = base58.b58encode(compressed).decode("utf-8")

    # URL encode
    url_encoded = urllib.parse.quote(encoded)

    # 输出订阅链接
    final_url = f"moontv://subscribe?data={url_encoded}"

    print("✅ Config validated and encoded successfully!")
    print("Your subscription URL:\n")
    print(final_url)

if __name__ == "__main__":
    main()
