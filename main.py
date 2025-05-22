def on_button_pressed_a():
    basic.show_string(control.device_name())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global mergedGraph
    mergedGraph = not (mergedGraph)
input.on_button_pressed(Button.B, on_button_pressed_b)

mergedGraph = False
mergedGraph = True
bluetooth.start_uart_service()

def on_forever():
    if mergedGraph:
        bluetooth.uart_write_value("a.x", input.acceleration(Dimension.X))
        bluetooth.uart_write_value("a.y", input.acceleration(Dimension.Y))
        bluetooth.uart_write_value("a.z", input.acceleration(Dimension.Z))
    else:
        bluetooth.uart_write_value("x", input.acceleration(Dimension.X))
        bluetooth.uart_write_value("y", input.acceleration(Dimension.Y))
        bluetooth.uart_write_value("z", input.acceleration(Dimension.Z))
basic.forever(on_forever)
