import time
import winsound
from win10toast import ToastNotifier


def timer(message, minutes):
    notificator = ToastNotifier()
    notificator.show_toast(
        "Alarm", f"Alarm will go off in {minutes} minutes..", duration=50)
