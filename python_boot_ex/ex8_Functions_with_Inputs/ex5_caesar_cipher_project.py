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
import ex5_caesar_art

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
game_chk = True

"""
step 1 encrypt, decrypt 만들기

def encrypt(en_text, en_shift):
    rs_char = ""
    for char in en_text:
        if char.isalpha():
            # 배열
            shifted_char_idx = alphabet.index(char) + en_shift
            if shifted_char_idx > 25:
                shifted_char_idx = shifted_char_idx - 26
            shifted_char = alphabet[shifted_char_idx]
            # 아스키코드
            # shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            shifted_char = char
        rs_char += shifted_char
    print(f"The encoded text is {rs_char}")


def decrypt(dn_text, dn_shift):
    de_char = ""
    for char in dn_text:
        if char.isalpha():
            # 배열
            shifted_char_idx = alphabet.index(char) - dn_shift
            if shifted_char_idx < 0:
                shifted_char_idx = 26 + shifted_char_idx
            shifted_char = alphabet[shifted_char_idx]
            # 아스키코드
            # shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            shifted_char = char
        de_char += shifted_char
    print(f"The decoded text is {de_char}")
"""

"""
step 2 encrypt, decrypt 하나로 합치기
"""


def caesar(plain_text, shift_number, en_type):
    result = ""
    if en_type == 'decode':
        shift_number *= -1

    for char in plain_text:
        char_idx = alphabet.index(char)
        shifted_char_idx = char_idx + shift_number
        if char.isalpha():
            if en_type == 'encode':
                if shifted_char_idx > 25:
                    shifted_char_idx = shifted_char_idx - 26
            elif en_type == 'decode':
                if shifted_char_idx < 0:
                    shifted_char_idx = 26 + shifted_char_idx
            shifted_char = alphabet[shifted_char_idx]
        else:
            shifted_char = char
        result += shifted_char
    print(f"The {en_type}d text is {result}")


print(ex5_caesar_art.logo)

while game_chk:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_number=shift % 26, en_type=direction)

    game_chk = False
    again = input("Type 'yes' if you want go again. Otherwise type 'no'\n")
    if again == 'yes':
        game_chk = True
    else:
        print("Good Bye")

