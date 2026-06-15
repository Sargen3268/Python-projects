import sys
print(sys.executable)

import time
from plyer import notification

while True:
    print("This is a reminder!")
    notification.notify(
        title="Reminder",
        message="Drink Water.",
        timeout=10  # Notification will disappear after 10 seconds
    )
    time.sleep(60*60)  # Wait for 60 seconds before printing the reminder again