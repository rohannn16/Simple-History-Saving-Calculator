FILE_HISTORY = "history.txt"

def show_history():
    with open(FILE_HISTORY, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("empty! No history found")
        else:
            print("_____CALCULATION HISTORY_____")
            for line in reversed(lines):
                print(line.strip())

def clear_history(): 
    with open(FILE_HISTORY, "w") as file: # This make file empty
        pass
    print("History cleared")

def save_to_history(equation, result):
    with open(FILE_HISTORY, "a") as file:
        # file.write(f"{equation} = {str(result)} \n")  
        file.write(f"{equation} = {result} \n")  

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input! Use formate: Number Operator Number (e.g:- 2 + 3)")
        return
    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter numeric value")

    if op == "+":
       result = num1 + num2
    elif op == "-":
       result = num1 - num2
    elif op == "*":
       result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("cannot divide by zero")
            return
        result = num1 / num2
    elif op == "%":
       result = num1 % num2
    else:
        print("Invalid operator! Use only this operator (+, -, *, /, %)")
    
    if result.is_integer(): #convert float to int(if it is already not in int)
        result = int(result)
    
    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("______SIMPLE HITORY SAVING CALCULATOR______")
    while True:
        user_input = input("Enter equation using these operator(+, -, *, /, %) or command(history, clear, exit): ").strip().lower()
        if user_input == "exit":
            print("You Exit!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()