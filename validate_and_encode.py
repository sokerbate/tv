import gzip
import base58
import urllib.parse

# 输入配置文件
with open("config.json", "rb") as f:
    data = f.read()

# 压缩
compressed = gzip.compress(data)

# Base58 编码
encoded = base58.b58encode(compressed).decode()

# URL encode
encoded_url = urllib.parse.quote(encoded)

# 拼接 MoonTV 订阅链接
final_url = f"moontv://subscribe?data={encoded_url}"

# 输出到文件
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(final_url)

print("✅ 订阅链接已生成：")
print(final_url)
