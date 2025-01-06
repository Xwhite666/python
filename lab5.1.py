
n = int(input("Введіть кількість елементів масиву: "))


array = []
print("Введіть елементи масиву:")
for _ in range(n):
    array.append(int(input()))


sum_positive_even = sum(x for x in array if x > 0 and x % 2 == 0)


print(f"Сума додатніх парних елементів масиву: {sum_positive_even}")
