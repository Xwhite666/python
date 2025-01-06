from collections import Counter

user_input = input("Введіть набір цифр: ")

count = Counter(user_input)

max_count = max(count.values())
result = {digit for digit, freq in count.items() if freq == max_count}

print("Цифри, які зустрічаються найбільше:", result)
