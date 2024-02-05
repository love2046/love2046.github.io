import sys
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        encoding = result['encoding']
        confidence = result['confidence']

        print(f"File encoding: {encoding} with confidence: {confidence * 100}%")

def convert_to_utf8(input_file, output_file):
    with open(input_file, 'r', encoding='gb2312', errors='ignore') as file:
        content = file.read()

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file_path = sys.argv[1]
        detect_encoding(input_file_path)
    elif len(sys.argv) == 3:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        with open(input_file_path, 'rb') as file:
            result = chardet.detect(file.read())
            encoding = result['encoding']
            if encoding.lower() != 'utf-8':
                convert_to_utf8(input_file_path, output_file_path)
            else:
                print("File is already in UTF-8 encoding.")
    else:
        print("Usage: python script.py input_file [output_file]")

