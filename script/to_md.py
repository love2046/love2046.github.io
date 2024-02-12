import os
from markdownify import markdownify as md

# 输入目录和输出目录
input_dir = "cmn"
output_dir = "mdcmn"

# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历输入目录中的所有HTML文件
for filename in os.listdir(input_dir):
    if filename.endswith(".htm"):
        # 构建输入文件路径和输出文件路径
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename[:-4] + ".md")

        # 读取HTML文件内容并转换为Markdown格式
        with open(input_path, "r", encoding="utf-8") as f_in:
            html_content = f_in.read()
            markdown_content = md(html_content)

        # 将Markdown内容写入输出文件
        with open(output_path, "w", encoding="utf-8") as f_out:
            f_out.write(markdown_content)

