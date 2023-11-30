"""
알파벳 시프트에 대한 계산 정리 - 아스키코드식
문자가 h, 시프트 숫자가 3일 때
1. ord(char) - ord('a'): 'h'의 ASCII 코드 값은 104이고, 'a'의 ASCII 코드 값은 97입니다. 따라서, 104 - 97 = 7이 됩니다.
2. (ord(char) - ord('a') + shift): 위에서 구한 값에 shift(3)을 더합니다. 7 + 3 = 10이 됩니다.
3. (ord(char) - ord('a') + shift) % 26: 위에서 구한 값을 26으로 나눈 나머지를 취합니다. 10 % 26 = 10이 됩니다.
4. ord('a'): 위에서 구한 나머지에 'a'의 ASCII 코드 값을 더합니다. 10 + 97 = 107이 됩니다.

배열식
알파벳 배열에서 문자의 index를 찾고
시프트 숫자를 더하거나 뺀다.
결과 인덱스가 25보다 클때는 -26, 작을때는 +26으로 결과 인덱스를 계산해준다.
"""


alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
game_chk = True

def encrypt(text, shift):
    rs_char = ""
    for char in text:
        if char.isalpha():
            # 배열
            shifted_char_idx = alphabet.index(char) + shift
            if shifted_char_idx > 25:
                shifted_char_idx = shifted_char_idx - 26
            shifted_char = alphabet[shifted_char_idx]
            # 아스키코드
            # shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            shifted_char = char
        rs_char += shifted_char
    print(f"The encoded text is {rs_char}")


def decrypt(text, shift):
    de_char = ""
    for char in text:
        if char.isalpha():
            # 배열
            shifted_char_idx = alphabet.index(char) - shift
            if shifted_char_idx < 0:
                shifted_char_idx = 26 + shifted_char_idx
            shifted_char = alphabet[shifted_char_idx]
            # 아스키코드
            # shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            shifted_char = char
        de_char += shifted_char
    print(f"The decoded text is {de_char}")


while game_chk:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text=text, shift=shift)
    elif direction == 'decode':
        decrypt(text=text, shift=shift)

    again = input("Type 'yes' if you want go again. Otherwise type 'no'\n")
    if again == 'no':
        game_chk = False

