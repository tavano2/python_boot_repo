import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_pd = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_pd)

result_dict = {row.letter: row.code for (index, row) in nato_pd.iterrows()}
# print(result_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
rs_input = input("Enter a word:")
rs_arr = [result_dict[item.upper()] for item in rs_input]
print(rs_arr)
