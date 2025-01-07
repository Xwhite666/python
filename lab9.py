import re

try:
    with open("TF14_1.txt", "w") as file1:
        file1.writelines([
            "123.45 This is a test 56 string\n",
            "Some more numbers like 0.89 and -12.3456\n",
            "No numbers here! Just text.\n",
            "Another line with 100.001 and 3.14\n"
        ])
    print("Файл TF14_1 успішно створено.")
except Exception as e:
    print(f"Помилка створення файлу TF14_1: {e}")

try:
    with open("TF14_1.txt", "r") as file1:
        content = file1.read()
        numbers = re.findall(r"[-+]?[0-9]*\.?[0-9]+", content)

    with open("TF14_2.txt", "w") as file2:
        file2.write(" ".join(numbers))
    print("Файл TF14_2 успішно створено з числами.")
except Exception as e:
    print(f"Помилка обробки файлів TF14_1 або TF14_2: {e}")

try:
    with open("TF14_2.txt", "r") as file2:
        numbers = list(map(float, file2.read().split()))
        max_number = max(numbers) if numbers else None

    if max_number is not None:
        print(f"Найбільше число у файлі TF14_2: {max_number}")
    else:
        print("Файл TF14_2 не містить чисел.")
except Exception as e:
    print(f"Помилка читання файлу TF14_2: {e}")
