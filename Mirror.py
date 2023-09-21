try:
    r = float(input("R: "))
    if r > 0:
        print(r * 2)
    else:
        print("Радіус має бути додатнім.")
except ValueError:
    print("Радіус має бути числом.")