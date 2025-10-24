def add_numbers(a, b):
    total = a + b
    return total

def divide_numbers(a, b):
    result = a / b
    return result

def main():
    x = 10
    y = 0
    sum_value = add_numbers(x, 5)
    print("Sum:", sum_value)
    div_value = divide_numbers(x, y)
    print("Division:", div_value)

if __name__ == "__main__":
    main()
    