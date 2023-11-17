
print('The Love Calculator is calculating your score...')
name1 = input()
name2 = input()

combined_names = name1 + name2
lover_names = combined_names.lower()

t = lover_names.count('t')
r = lover_names.count('r')
u = lover_names.count('u')
e = lover_names.count('e')
first_digit = t + r + u + e

l = lover_names.count('l')
o = lover_names.count('o')
v = lover_names.count('e')
twice_digit = l + o + v + e

score = int(str(first_digit) + str(twice_digit))

if (score < 10) or (score > 90):
    print(f'Your score is {score}, You go together like coke and mentos')
elif (score >= 40) or (score <= 50):
    print(f'Your score is {score}, You are alright together')
else:
    print(f'Your score is {score}')