alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet += ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def to_caesar(text, shift):
    result = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift 
        result += alphabet[new_position]
    return result

def transpose(text, key): 
    key_length = len(key)
    blocks = [text[i : i + key_length] for i in range(0, len(text), key_length)]
    cipher = ""
    for block in blocks:
        for i in range(0, key_length):
            cipher += block[key[i] - 1]
    return cipher


msg = "MOTIVATION"
s1 = to_caesar(msg.lower(), 17)
print(s1)
p1 = transpose(s1.lower(), [5, 1, 3, 2, 4])
print(p1)
s2 = to_caesar(p1.lower(), 8)
print(s2)
p2 = transpose(s2.lower(), [3, 4, 5, 1 ,2])
print(f"The final ciphertext is: {p2}")
