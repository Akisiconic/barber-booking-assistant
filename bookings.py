# bookings.py - handles booking, rescheduling and cancelling appointments
booked_slots = [9, 10, 11]
hour = 10
open_time = 9
close_time = 18
lunch_time = 12
day = "monday"

def find_next_slot(booked_slots):
    for time_slot in range(9, 18):
        if time_slot == lunch_time:
            continue
        if time_slot in booked_slots:
            continue
        return time_slot
    else:
        return None
booked_slots = [9,10,11,13,14,15,16,17]
print(find_next_slot(booked_slots))

if day.lower() == "sunday":
    print("We are closed today ")
elif hour >= close_time:
    print("shop is closed")
elif hour == lunch_time:
    print("Barber is on lunch, back at 1")
elif hour >= open_time:
    print("shop is open")
    for time_slot in range(9, 18):
        if time_slot == lunch_time:
            continue
        if time_slot not in booked_slots:
            print(f"Next Available: {time_slot}:00") 
            break 
    else:
        print("No Slots available Today") 
else:
    print("We are still closed right now !")



