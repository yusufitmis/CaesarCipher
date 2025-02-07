# Caesar Cipher - README

## **Description / Açıklama:**

This project aims to encrypt and decrypt messages using the **Caesar Cipher** algorithm. The Caesar Cipher works by shifting each letter of the message by a fixed number. This project includes both encryption and decryption functions.

Bu proje, **Caesar Cipher** (Sezar Şifrelemesi) algoritmasını kullanarak mesajları şifreleyip çözmeyi amaçlar. Caesar Cipher, her harfi belirli bir sayı kadar kaydırarak şifreleme yapan basit bir algoritmadır. Bu projede hem şifreleme (encryption) hem de şifre çözme (decryption) işlevleri bulunmaktadır.

## **Functions / Fonksiyonlar:**

### 1. `CaesarCiphers(plainMessage, k)`
- This function encrypts the given plain text message.
- **`plainMessage`**: The message to be encrypted (e.g., `"HELLO WORLD"`).
- **`k`**: The number of positions each letter should be shifted (e.g., `7`).
- **Output**: The encrypted message.

### 2. `CaesarCiphersDecrypton(ciphernMessage, k)`
- This function decrypts the given cipher text message.
- **`cipherMessage`**: The message to be decrypted (e.g., `"OLSSV DVYSK"`).
- **`k`**: The number of positions each letter should be shifted (e.g., `7`).
- **Output**: The encrypted message.

**Example:**
```python
CaesarCiphers("HELLO WORLD", 7)
# Output: "OLSSV DVYSK"
```
![image](https://github.com/yusufitmis/CaesarCipher/blob/main/image.PNG) 


