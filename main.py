// Pin assignments
let servoPin = AnalogPin.P0;
let irSensorPin = DigitalPin.P1;
let ultrasonicTriggerPin = DigitalPin.P2;
let ultrasonicEchoPin = DigitalPin.P8;

// Constants
const blackThreshold = 1;
const distanceThreshold = 20;

// Servo motor control
function setServoAngle(angle: number) {
    let pulseWidth = Math.map(angle, 0, 180, 500, 2400);
    pins.servoWritePin(servoPin, pulseWidth);
}

// Function to hit the black object towards the right side
function hitObjectRight() {
    setServoAngle(30);
    basic.pause(1000);
    setServoAngle(90);
}

// Function to hit the white object towards the left side
function hitObjectLeft() {
    setServoAngle(150);
    basic.pause(1000);
    setServoAngle(90);
}

// Function to stop the servo motor
function stopServoMotor() {
    setServoAngle(90);
}

// Main program
basic.forever(function () {
    let irSensorValue = pins.digitalReadPin(irSensorPin);
    let distance = sonar.ping(
        ultrasonicTriggerPin,
        ultrasonicEchoPin,
        PingUnit.Centimeters
    );

    if (irSensorValue === blackThreshold && distance < distanceThreshold) {
        hitObjectRight();
    } else if (irSensorValue !== blackThreshold && distance < distanceThreshold) {
        hitObjectLeft();
    }
});
