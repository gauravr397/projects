import time
import winsound
from win10toast import ToastNotifier


def timer(message, minutes):
    notificator = ToastNotifier()
    notificator.show_toast(
        "Alarm", f"Alarm will go off in {minutes} minutes..", duration=50)
    time.sleep(minutes*60)
    winsound.beep(frequency=2500, duration=1000)
    notificator.show_toast(f"alarm", message, duration=50)


if __name__ == "__main__":
    message = "Workout !"
    minutes = 1
    timer(message, minutes)
