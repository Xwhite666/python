
input_string = input("Введіть рядок: ")

if len(input_string) >= 21:

    result = input_string[:21:5]
    print("Кожний 5-й символ до 21-го:", result)
else:
    print("Рядок занадто короткий для виконання операції.")
