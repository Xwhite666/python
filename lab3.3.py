
sentence = input("Введіть речення: ")


words = sentence.split()


max_length = max(len(word) for word in words)


if max_length > 10:
    print("Твердження правдиве: найдовше слово має більше 10 символів.")
else:
    print("Твердження хибне: найдовше слово не має більше 10 символів.")
