import platformio

board = "arduino:avr:uno"
platform = "atmega328p"

led_pin = 13

serial = platformio.serial_open("/dev/ttyUSB0",9600)

platformio.core.pins.pinMode(board, led_pin, platformio.core.pins.OUTPUT)

#blink LED
while True:
    platformio.core.pins.digitalWrite(board, led_pin, 1)
    time.sleep(1)
    platformio.core.pins.digitalWrite(board, led_pin, 0)
    time.sleep(1)
    
serial.close()
