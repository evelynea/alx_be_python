def perform_operation(num1, num2, operation):
    match operation:
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
            elif num2 != 0:
                return num1 / num2
        case "_":
            print("not an acceptable operation")
