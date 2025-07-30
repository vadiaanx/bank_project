new_list = []

while len(new_list) < 3:
    user_input = input(f"Введи число {len(new_list)+1}: ")
    try:
        num = int(user_input)
    except ValueError:
        print("Ты ввёл не число")
        continue

    if num in new_list:
        print("Такое число уже есть. Оно не добавилось")
        continue

    new_list.append(num)

print(f"Уникальные числа: {new_list}")

with open("tasks.txt", "w", encoding="utf-8") as file:
    for x in new_list:
        file.write(f"{x}\n")