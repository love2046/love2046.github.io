import os
import sys
import chardet

def convert_to_utf8(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        result = chardet.detect(content)

    if result and result['encoding']:
        encoding = result['encoding']

        # 如果不是UTF-8编码，则进行转换
        if encoding.lower() != 'utf-8':
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content.decode(encoding, errors='replace'))
                print(f"Converted {os.path.basename(file_path)} to UTF-8")
            except UnicodeDecodeError as e:
                print(f"Error converting {os.path.basename(file_path)}: {e}")
        else:
            print(f"{os.path.basename(file_path)} is already in UTF-8 encoding.")
    else:
        print(f"Failed to detect encoding for {os.path.basename(file_path)}.")

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".txt"):
                file_path = os.path.join(root, filename)
                convert_to_utf8(file_path)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory_path = sys.argv[1]
        process_directory(directory_path)
    else:
        print("Usage: python script.py directory_path")

