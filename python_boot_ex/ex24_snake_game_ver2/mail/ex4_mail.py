PLACEHOLDER = "[name]"


# read names
with open("./Input/Names/invited_names.txt", mode="r") as mail_names:
    while True:
        line = mail_names.readline()
        if not line:
            break
        merge_name = line.strip()

        # read letter
        with open("./Input/Letters/starting_letter.txt", mode="r") as mail_letters:
            # for index, letter in enumerate(mail_letters):
            #     if index == 0:
            #         w_str = letter.replace(PLACEHOLDER, merge_name)
            #     else:
            #         w_str = letter
            #     # write letter
            #     with open("./Output/ReadyToSend/" + "letter_for_" + merge_name + ".txt", mode="a") as write_letters:
            #         write_letters.write(w_str)
            contents = mail_letters.read()
            new_letter = contents.replace(PLACEHOLDER, merge_name)
            with open("./Output/ReadyToSend/" + "letter_for_" + merge_name + ".txt", mode="a") as write_letters:
                write_letters.write(new_letter)

"""
솔루션 정답에서는
    1. mail_names를 readlines로 받아 배열로 반환하여 처리했다.
    2. letter를 열고 read 메소드로 문자열 전체를 반환하여 replace 처리를 진행했다.
"""