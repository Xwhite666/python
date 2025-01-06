
magazines = {
    "Журнал A": {"price": 12.5, "circulation": 8000},
    "Журнал B": {"price": 15.0, "circulation": 15000},
    "Журнал C": {"price": 10.0, "circulation": 5000},
    "Журнал D": {"price": 20.0, "circulation": 20000},
    "Журнал E": {"price": 18.0, "circulation": 7000}
}


def display_all(magazines):
    for name, info in magazines.items():
        print(f"{name}: Ціна - {info['price']} грн, Тираж - {info['circulation']} примірників")


def add_entry(magazines):
    name = input("Введіть назву журналу: ")
    price = float(input("Введіть ціну журналу: "))
    circulation = int(input("Введіть тираж журналу: "))
    magazines[name] = {"price": price, "circulation": circulation}
    print(f"Журнал '{name}' додано в базу.")


def remove_entry(magazines):
    name = input("Введіть назву журналу для видалення: ")
    if name in magazines:
        del magazines[name]
        print(f"Журнал '{name}' видалено з бази.")
    else:
        print(f"Журнал '{name}' не знайдено.")


def display_sorted(magazines):
    sorted_keys = sorted(magazines.keys())
    for name in sorted_keys:
        print(f"{name}: Ціна - {magazines[name]['price']} грн, Тираж - {magazines[name]['circulation']} примірників")


def average_price_under_10000(magazines):
    total_price = 0
    count = 0
    for info in magazines.values():
        if info["circulation"] < 10000:
            total_price += info["price"]
            count += 1
    if count > 0:
        return total_price / count
    else:
        return 0


def main():
    while True:
        print("\nМеню:")
        print("1. Вивести всі журнали")
        print("2. Додати журнал")
        print("3. Видалити журнал")
        print("4. Переглянути журнали за відсортованими назвами")
        print("5. Обчислити середню вартість журналів з тиражем менше 10000 примірників")
        print("6. Вихід")

        choice = input("Виберіть опцію (1-6): ")

        if choice == "1":
            display_all(magazines)
        elif choice == "2":
            add_entry(magazines)
        elif choice == "3":
            remove_entry(magazines)
        elif choice == "4":
            display_sorted(magazines)
        elif choice == "5":
            avg_price = average_price_under_10000(magazines)
            if avg_price > 0:
                print(f"Середня вартість журналів з тиражем менше 10000 примірників: {avg_price} грн.")
            else:
                print("Немає журналів з тиражем менше 10000 примірників.")
        elif choice == "6":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
