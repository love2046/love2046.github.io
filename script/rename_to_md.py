import os
import sys

def change_file_extension(file_path):
    # 修改文件扩展名为.md
    new_file_path = os.path.splitext(file_path)[0] + '.md'
    os.rename(file_path, new_file_path)
    print(f"Changed file extension for {os.path.basename(file_path)} to .md")

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".txt"):
                file_path = os.path.join(root, filename)

                # 修改文件扩展名为.md
                change_file_extension(file_path)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory_path = sys.argv[1]
        process_directory(directory_path)
    else:
        print("Usage: python script.py directory_path")

