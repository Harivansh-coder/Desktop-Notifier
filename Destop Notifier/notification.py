"""
An simple desktop notifier (notify to take break) every 2 hrs.
you can personalize it your own way.
"""
import time
from plyer import notification

if __name__ == "__main__":

    screen_time = 2  #screen time variable

    while True:
        if screen_time <= 8:
            notification.notify(
                title = "Dont forget to take break",
                message = "screen time = "+str(screen_time)+" hrs",

                timeout = 10 
            )
        else:
            notification.notify(
                title = "Stop it now it already more than 8 hrs",
                message = "screen time = "+str(screen_time)+" hrs using computer this much is not good for health",

                timeout = 10 
            )
        screen_time += 2

        time.sleep(60*60*2)