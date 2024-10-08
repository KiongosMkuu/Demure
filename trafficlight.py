def traffic_light_action(color):
    match color:
        case "red":
            return "Stop!"
        case "yellow":
            return "Prepare to stop."
        case "green":
            return "Go!"
        case _:
            return "Invalid traffic light color."


light_color = "yellow"
print(traffic_light_action(light_color))  
