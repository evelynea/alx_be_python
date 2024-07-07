def perform_operation(num1, num2, operations):
    match operations:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                print("cannot divide by 0")
                return
            else:
                return num1 / num2
        case "_":
            print("not an acceptable operation")
