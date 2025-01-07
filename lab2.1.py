import math

def calculate_z(x):
    if x > 45:
        return -math.sqrt(x)
    else:
        return math.sin(2 * x)

def find_fibonacci(p):
    f1, f2 = 0, 1
    while f2 <= p:
        f1, f2 = f2, f1 + f2
    return f2

def main():

    x = float(input("Введіть число x: "))
    z = calculate_z(x)
    print(f"Результат z: {z}")


    p = int(input("Введіть число p: "))
    fibonacci_number = find_fibonacci(p)
    print(f"Перше число Фібоначчі більше за {p}: {fibonacci_number}")

if __name__ == "__main__":
    main()
