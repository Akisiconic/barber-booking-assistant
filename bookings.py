# bookings.py - handles booking, rescheduling and cancelling appointments
hour = 20 
open_time = 9
close_time = 18

if hour >= close_time:
    print("shop is closed")
elif hour >= open_time:
    print("shop is open")

else:
    print("We are still closed right now")