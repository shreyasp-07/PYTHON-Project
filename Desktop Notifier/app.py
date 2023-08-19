from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message=f"You have to take rest on {time.strftime('%H:%M')}",
            timeout=5
        )
        time.sleep(60*60)

# pythonw app.py -> To run python in background