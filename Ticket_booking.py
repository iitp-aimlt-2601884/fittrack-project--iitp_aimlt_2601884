threatre_capacity = 350
minimum_age = 12
max_booking_per_person = 15

remaining_seats = threatre_capacity
total_bookings = 0
total_tickets_sold  = 0
rejected_bookings = 0

while remaining_seats > 0:
    print(f"Remaining Seats: {remaining_seats}")
    num_tickets = int(input("Enter the number of tickets to book: "))
    if num_tickets == 0:
        break

    if num_tickets > remaining_seats:
        print("BOOKING REJECTED - there are not enough seats available.")
        rejected_bookings += 1
        continue

    if num_tickets > max_booking_per_person:
        print(f"BOOKING REJECTED - cannot book more than {max_booking_per_person} tickets.")
        rejected_bookings += 1
        continue

    all_ages_valid = True
    for i in range(num_tickets):
        age = int(input(f"Enter age of the person {i+1}: "))
        if age < minimum_age:
            print("BOOKING REJECTED - age restriction.")
            rejected_bookings += 1
            all_ages_valid = False
            break
        if not all_ages_valid:            
             continue
    
    print(f"BOOKING CONFIRMED - {num_tickets} tickets.")
    total_bookings += 1
    total_tickets_sold += num_tickets
        
    if remaining_seats == 0:
        print("THEATRE FULL - no more bookings.")
        break

        
    print("\n--- FINAL REPORT ---")
    print("Total Bookings:", total_bookings)
    print("Total Tickets Sold:", total_tickets_sold)
    print("Rejected Bookings:", rejected_bookings)
    print("Remaining Seats:", remaining_seats)

