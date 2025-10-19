from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

leftMotor = Motor(19, 20, pwm=True)
rightMotor = Motor(11, 12, pwm=True)

if __name__ == '__main__':
    leftMotor.value(1)
    sleep(2)
    leftMotor.value(0)
