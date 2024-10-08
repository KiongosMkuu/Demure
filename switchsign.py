def handle_sign(sign):
    match sign:
        case "Stop":
            press_break()
        case "Merge":
            accelerate()
        case "Exit":
            decelerate()
        case _:
            ignore()

def press_break():
    print("Braking!")

def accelerate():
    print("Accelerating!")

def decelerate():
    print("Decelerating!")

def ignore():
    print("Ignoring sign.")

# Test the function
sign = "Stop"
handle_sign(sign)
