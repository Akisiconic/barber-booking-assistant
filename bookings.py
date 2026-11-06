# bookings.py - handles booking, rescheduling and cancelling appointments
hour = 10
open_time = 9
close_time = 18
lunch_time = 12
day = "monday"

if day.lower() == "sunday":
    print("We are closed today ")
elif hour >= close_time:
    print("shop is closed")
elif hour == lunch_time:
    print("Barber is on lunch, back at 1")
elif hour >= open_time:
    for time_slot in range(9, 18):
     print(f"{time_slot}:00 is Available")
    print("shop is open")
else:
    print("We are still closed right now !")



