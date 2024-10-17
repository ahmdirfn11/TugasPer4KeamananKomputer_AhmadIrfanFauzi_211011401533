def vigenere_encrypt(plaintext, keyword):
    encrypted = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for p_char, k_char in zip(plaintext, keyword_repeated):
        if p_char.isalpha():
            shift = ord(k_char.lower()) - ord('a')
            if p_char.islower():
                encrypted_char = chr((ord(p_char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(p_char) - ord('A') + shift) % 26 + ord('A'))
            encrypted.append(encrypted_char)
        else:
            encrypted.append(p_char)  # Non-alphabet characters remain unchanged

    return ''.join(encrypted)

def vigenere_decrypt(ciphertext, keyword):
    decrypted = []
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for c_char, k_char in zip(ciphertext, keyword_repeated):
        if c_char.isalpha():
            shift = ord(k_char.lower()) - ord('a')
            if c_char.islower():
                decrypted_char = chr((ord(c_char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(c_char) - ord('A') - shift) % 26 + ord('A'))
            decrypted.append(decrypted_char)
        else:
            decrypted.append(c_char)  # Non-alphabet characters remain unchanged

    return ''.join(decrypted)

# Contoh penggunaan
if __name__ == "__main__":
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")
    keyword = input("Masukkan kata kunci: ")

    encrypted_text = vigenere_encrypt(plaintext, keyword)
    print(f"Teks terenkripsi: {encrypted_text}")

    decrypted_text = vigenere_decrypt(encrypted_text, keyword)
    print(f"Teks setelah dekripsi: {decrypted_text}")
