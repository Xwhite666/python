
word = input("Введіть слово: ")


if any(char.isdigit() for char in word):
    print("У слові є цифри.")
else:
    print("У слові немає цифр.")
