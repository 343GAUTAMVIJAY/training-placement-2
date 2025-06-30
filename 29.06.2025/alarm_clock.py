import time
import winsound  # Use `os.system('afplay /System/Library/Sounds/Ping.aiff')` on macOS

seconds = int(input("Enter alarm time in seconds: "))
time.sleep(seconds)
winsound.Beep(1000, 1000)  # Frequency, duration
print("Alarm!")