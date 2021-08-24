import re

s = "还来客89BBQ"

uncn_en = re.compile(r'[\u0061-\u007a,\u0020]')
en = "".join(uncn_en.findall(s.lower()))

# uncn_zh = re.compile(r'[\u4e00-\u9fa5]')
# zh = "".join(uncn_zh.findall(s.lower()))

uncn_zh = re.compile(r'[^\u0061-\u007a,\u0020]')
zh = "".join(uncn_zh.findall(s.lower()))

print(en)
print(zh)

# 中文的编码范围是：\u4e00-\u9fa5，相应的[^\u4e00-\u9fa5]可匹配非中文。
# 匹配英文时，需要将空格[\u0020]加入，不然单词之间没空格了。