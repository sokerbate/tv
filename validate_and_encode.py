import json
import base58

# 统一的防盗链 headers
HEADERS = {
    "Referer": "https://tv.sokerbate.shop/",  # 这里换成你的域名
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# 读取 config.json
with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 给每个视频源加 headers
for item in data:
    item["headers"] = HEADERS

# 校验 JSON 是否正确
try:
    json_str = json.dumps(data, ensure_ascii=False)
except Exception as e:
    print("JSON 校验失败:", e)
    exit(1)

# 转成 Base58
encoded = base58.b58encode(json_str.encode("utf-8")).decode("utf-8")

# 输出到 output.txt
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(encoded)

print("生成成功: output.txt（已加 headers）")
