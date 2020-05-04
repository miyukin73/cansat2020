import led_class

green_led=led_class.Led(25)
blue_led=led_class.Led(24)
i=0

try:
    while i<4:
        green_led.led_on()
        blue_led.led_off()
        led_class.sleep(0.5)
        green_led.led_off()
        blue_led.led_on()
        led_class.sleep(0.5)
        i+=1
        
except KeyboardInterrupt:
    pass

green_led.led_off()
blue_led.led_off()

led_class.clean_up()