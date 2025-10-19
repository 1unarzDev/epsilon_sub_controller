from gpiozero import Motor, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

Device.pin_factory = LGPIOFactory()

leftMotor = Motor(19, 20, pwm=True)
rightMotor = Motor(11, 12, pwm=True)

if __name__ == '__main__':
    leftMotor.forward()
    rightMotor.forward()
    sleep(2)
    leftMotor.stop()
    rightMotor.stop()