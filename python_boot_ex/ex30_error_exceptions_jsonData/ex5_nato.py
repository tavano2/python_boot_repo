import pandas

nato_pd = pandas.read_csv("nato_phonetic_alphabet.csv")

result_dict = {row.letter: row.code for (index, row) in nato_pd.iterrows()}


def nato_phonetic_alphabet():
    try:
        rs_input = input("Enter a word:")
        rs_arr = [result_dict[item.upper()] for item in rs_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_phonetic_alphabet()
    else:
        print(rs_arr)


nato_phonetic_alphabet()
