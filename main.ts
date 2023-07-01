let ir_sensor = 0
pins.servoWritePin(AnalogPin.P2, 90)
basic.forever(function () {
    ir_sensor = 0
    serial.writeString("\"x\"")
})
