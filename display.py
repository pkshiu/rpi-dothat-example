import atexit
import time
from dothat import lcd, backlight


def tidyup():
    backlight.off()
    backlight.graph_off()
    lcd.clear()


atexit.register(tidyup)

backlight.rgb(0, 255, 0)
lcd.set_cursor_position(0, 0)
lcd.write('Hello LCD')

while(1):
    lcd.set_cursor_position(0,1)
    lcd.write(time.asctime()[:10])
    lcd.set_cursor_position(0,2)
    lcd.write(time.asctime()[11:])
    backlight.set_graph(time.time() % 1)
    time.sleep(1)




