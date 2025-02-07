
def CaesarCiphers(plainMessage,k):
    plainWords = plainMessage.split()
    ciphersMap = {"A":0 , "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, 
                  "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
    reverseMap = {v: k for k, v in ciphersMap.items()}
    cipherWords = ""
    for plainWord in plainWords:
        cipherWord = ""
        for plainLetter in plainWord:
            plainNumber= ciphersMap[plainLetter]
            cipherNumber = (plainNumber + k) % 26
            cipherLetter = reverseMap[cipherNumber]
            cipherWord = cipherWord + cipherLetter
        cipherWords = cipherWords.lstrip(" ") + " " + cipherWord
    print(cipherWords)

def CaesarCiphersDecrypton(cipherMessage,k):
    cipherWords = cipherMessage.split()
    ciphersMap = {"A":0 , "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, 
                  "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
    reverseMap = {v: k for k, v in ciphersMap.items()}
    plainWords = ""
    for cipherWord in cipherWords:
        plainWord = ""
        for cipherLetter in cipherWord:
            cipherNumber= ciphersMap[cipherLetter]
            plainNumber = (cipherNumber - k) % 26
            plainLetter = reverseMap[plainNumber]
            plainWord = plainWord + plainLetter
        plainWords = plainWords.lstrip(" ") + " " + plainWord
    print(plainWords)

def Main():
    CaesarCiphers("HELLO WORLD",7)
    CaesarCiphersDecrypton("OLSSV DVYSK",7)

Main()