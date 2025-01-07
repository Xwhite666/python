import json

journals = [
    {"Name": "Журнал 1", "Price": 50, "Circulation": 12000},
    {"Name": "Журнал 2", "Price": 60, "Circulation": 5000},
    {"Name": "Журнал 3", "Price": 45, "Circulation": 8000},
    {"Name": "Журнал 4", "Price": 70, "Circulation": 15000},
    {"Name": "Журнал 5", "Price": 40, "Circulation": 7000}
]

jsonData = json.dumps(journals, ensure_ascii=False, indent=4)
with open("journals.json", "wt", encoding="utf-8") as file:
    file.write(jsonData)

while True:
    print(
        "Оберіть опцію:\n 1 - Додати дані\n 2 - Переглянути дані\n 3 - Знайти журнали з тиражем < 10000\n 4 - Обчислити середню ціну для журналів з тиражем < 10000\n 5 - Вийти")
    x = input("Оберіть опцію:\n")
    x = int(x)


    if x == 1:
        with open("journals.json", "at", encoding="utf-8") as file:

            file.seek(0)
            journals = json.load(file)


            def add_journal(data):
                print("Додати новий журнал: ")
                name = input("Назва: ")
                price = float(input("Ціна: "))
                circulation = int(input("Тираж: "))
                data.append({"Name": name, "Price": price, "Circulation": circulation})
                return data


            journals = add_journal(journals)
            jsonData = json.dumps(journals, ensure_ascii=False, indent=4)
            file.seek(0)
            file.truncate()
            file.write(jsonData)

    if x == 2:
        with open("journals.json", "rt", encoding="utf-8") as file:
            journals = json.load(file)
            print("Список всіх журналів:")
            print(*journals, sep='\n')

    if x == 3:
        with open("journals.json", "rt", encoding="utf-8") as file:
            journals = json.load(file)
            small_circulation = [journal for journal in journals if journal['Circulation'] < 10000]
            print("Журнали з тиражем менше 10000:")
            print(*small_circulation, sep='\n')

    if x == 4:
        with open("journals.json", "rt", encoding="utf-8") as file:
            journals = json.load(file)
            small_circulation_journals = [journal for journal in journals if journal["Circulation"] < 10000]
            if small_circulation_journals:
                avg_price = sum(journal["Price"] for journal in small_circulation_journals) / len(
                    small_circulation_journals)
                print(f"Середня ціна журналів з тиражем менше 10000: {avg_price:.2f}")

                result_data = {"average_price_for_small_circulation": avg_price}
                with open("average_price_result.json", 'w', encoding='utf-8') as result_file:
                    json.dump(result_data, result_file, ensure_ascii=False, indent=4)
                print("Результат збережено у файл 'average_price_result.json'.")
            else:
                print("Немає журналів з тиражем менше 10000.")

    if x == 5:
        print("Вихід з програми.")
        quit(0)
