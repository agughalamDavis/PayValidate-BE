def add_digits(digit) -> int:
    sum = 0
    digit = str(digit)
    for char in digit:
        sum += int(char)
    return sum


def luhns_algorithm(card_number: str) -> int:
    doubled = []
    check_numbers = card_number[0:-1]

    #get step digits to multiply
    index = len(check_numbers)-1
    while index >= 0 :
        doubled.append((int(check_numbers[index]) * 2))
        doubled.append(check_numbers[index-1])
        index -= 2

    #add digits
    total = sum(list(map(lambda x: add_digits(x), doubled)))

    final_digit = 10 - (total%10)

    return final_digit

