from collections import defaultdict

def build_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def read_text_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def build_c_array(bwt):
    c = {}
    sorted_bwt = sorted(bwt)
    for char in set(bwt):
        c[char] = sorted_bwt.index(char)
    return c

def build_occur_table(bwt):
    occur = defaultdict(lambda: [0] * (len(bwt) + 1))
    for i in range(1, len(bwt) + 1):
        char = bwt[i - 1]
        for c in occur:
            occur[c][i] = occur[c][i - 1] + (1 if c == char else 0)
        occur[char][i] = occur[char][i - 1] + 1
    return occur

def build_bwt(text, suffix_array):
    return ''.join([text[i - 1] for i in suffix_array])

def inverse_bwt(bwt):
    c = build_c_array(bwt)
    occur = build_occur_table(bwt)
    original = []
    index = 0
    
    for _ in range(len(bwt)):
        char = bwt[index]
        original.append(char)
        index = c[char] + occur[char][index]
    
    return ''.join(original[::-1])

def backward_search(bwt, c, occur, pattern):
    sp = 0
    ep = len(bwt) - 1

    for char in reversed(pattern):
        if char not in c:
            return -1 
        
        sp = c[char] + occur[char][sp]
        ep = c[char] + occur[char][ep + 1] - 1
        
        if sp > ep:
            return -1 
    
    return sp, ep

if __name__ == "__main__":
    filename = "example.txt"
    text = read_text_file(filename)

    if not text.endswith('$'):
        text += '$'
        
    suffix_array = build_suffix_array(text)
    print("Suffix Array:", suffix_array)
    
    bwt = build_bwt(text, suffix_array)
    print("BWT:", bwt)

    c = build_c_array(bwt)
    occur = build_occur_table(bwt)
    print("C array:", c)
    print("Occur table:", dict(occur))

    original_text = inverse_bwt(bwt)
    print("Texto original reconstruido:", original_text)

    pattern = "ana"
    result = backward_search(bwt, c, occur, pattern)
    
    if result != -1:
        sp, ep = result
        print(f"El patrón '{pattern}' se encuentra entre las posiciones {sp} y {ep}.")
    else:
        print(f"El patrón '{pattern}' no se encuentra en la cadena.")






