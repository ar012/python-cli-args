def input_Number(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass

    return num