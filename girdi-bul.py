def find_numbers(numbers, result):
    numbers = input("Enter the numbers with spaces in-between: ").split()
    result = int(input("Enter the result: "))
    numbers = [int(i) for i in numbers]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == result:
                return [numbers[i], numbers[j]]


while True:
    numbers = []
    result = 0
    numbers = find_numbers(numbers, result)

    if numbers is None:
        print("No numbers found!")
    else:
        print("You can get the result by adding these numbers together: ", numbers)

    if input("Do you want to restart? (y/n): ") == "n":
        print("Exiting...")
        break
