from collections import defaultdict

def build_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def read_text_file(filename):
    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    filename = "example.txt"
    text = read_text_file(filename)

    if not text.endswith('$'):
        text += '$'

    suffix_array = build_suffix_array(text)
    print("Suffix Array:", suffix_array)
