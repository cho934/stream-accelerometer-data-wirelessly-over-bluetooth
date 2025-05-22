input.onButtonPressed(Button.A, function () {
    basic.showString(control.deviceName())
})
input.onButtonPressed(Button.B, function () {
    mergedGraph = !(mergedGraph)
})
let mergedGraph = false
mergedGraph = true
bluetooth.startUartService()
basic.forever(function () {
    if (mergedGraph) {
        bluetooth.uartWriteValue("a.x", input.acceleration(Dimension.X))
        bluetooth.uartWriteValue("a.y", input.acceleration(Dimension.Y))
        bluetooth.uartWriteValue("a.z", input.acceleration(Dimension.Z))
    } else {
        bluetooth.uartWriteValue("x", input.acceleration(Dimension.X))
        bluetooth.uartWriteValue("y", input.acceleration(Dimension.Y))
        bluetooth.uartWriteValue("z", input.acceleration(Dimension.Z))
    }
})
