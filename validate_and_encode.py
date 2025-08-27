import json
import sys
import base58

def validate_and_encode(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)  # 如果不是合法 JSON 会报错
    except Exception as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)

    # 转成字符串再编码
    json_str = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    encoded = base58.b58encode(json_str.encode("utf-8")).decode("utf-8")

    print("✅ JSON is valid.")
    print(f"🔑 Base58 encoded result:\n{encoded}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_and_encode.py <file.json>")
        sys.exit(1)
    validate_and_encode(sys.argv[1])
