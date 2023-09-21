worms = 2          # Початкова кількість черв'яків
period = 10
max_time = 142840  # Обмежуємо max_time з метою запобігання зависання при розрахунках

try:
    time = int(input(f"Введіть час в хвилинах від 0 до {max_time}: "))

    if time < 0:
        print("Час має бути додатнім.")
    elif time > max_time:
        print("Час завеликий. Спробуйте менше значення.")
    else:
        result = worms ** (1 + time // period)
        try:
            print(result)
        except ValueError:
             print("Результат завеликий, неможливо роздрукувати")

except ValueError:
    print("Час має бути цілим числом.")