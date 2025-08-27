import json
import base58

# 读取 config.json
with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 自动为每个 api_site 添加统一 headers
default_headers = data.get("headers", {})
for site in data.get("api_site", {}).values():
    site["headers"] = default_headers

# 校验 JSON
try:
    json_str = json.dumps(data, ensure_ascii=False)
except Exception as e:
    print("JSON 校验失败:", e)
    exit(1)

# 转 Base58
encoded = base58.b58encode(json_str.encode("utf-8")).decode("utf-8")

# 输出到 output.txt
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(encoded)

print("生成成功: output.txt")
