
def remove_odd_index_elements(input_list):

    return [input_list[i] for i in range(len(input_list)) if i % 2 == 0]

user_input = input("Введіть елементи списку через пробіл: ")
input_list = list(map(int, user_input.split()))

modified_list = remove_odd_index_elements(input_list)

print("Модифікований список:", modified_list)
