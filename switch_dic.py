def handle_sign(sign):
    actions = {
        "Stop": press_break,
        "Merge": accelerate,
        "Exit": decelerate
    }

    # Call the appropriate function or ignore if not found
    action = actions.get(sign, ignore)
    action()

def press_break():
    print("Braking!")

def accelerate():
    print("Accelerating!")

def decelerate():
    print("Decelerating!")

def ignore():
    print("Ignoring sign.")

# Test the function
sign = "Exit"
handle_sign(sign)
