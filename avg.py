numbers = []
while True:
    user_input = input("Enter a number (or 'close' to finish): ")
    
    if user_input == "close":
        if numbers:
            average = sum(numbers) / len(numbers)
            print("Average:", average)
        else:
            print("No numbers entered.")
        break
    
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'close'.")
        continue

