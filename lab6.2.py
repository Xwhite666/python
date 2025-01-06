
def sum_of_elements(input_list):
    return sum(input_list)

user_input = input("Введіть елементи списку через пробіл: ")
input_list = list(map(int, user_input.split()))

total_sum = sum_of_elements(input_list)

print("Сума елементів списку:", total_sum)
