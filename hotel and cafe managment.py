import random  # Import random module to generate random room numbers
print("hotel and cafe managment")  

# Dictionary to store different room types with their prices
room_types = {"1": {"type": "single bed room", "price": 1000},
              "2": {"type": "queen size bed room", "price": 1500},
              "3": {"type": "king size bed family suite", "price": 2500}}

# Dictionary to store food menu for different meals
food_menu = {"breakfast": {"1": {"name": "prantha", "price": 50},
                           "2": {"name": "bread omelete", "price": 60},
                           "3": {"name": "poha", "price": 40}},

             "lunch": {"rice with daal makhani": 120,
                       "rice with paneer butter masala": 150,
                       "rice with butter chicken": 180,
                       "naan bread with dal tadka": 100,
                       "naan bread with paneer tikka masala": 130,
                       "naan bread with lamb rogan josh": 200,
                       "veg biryani": 140,
                       "non-veg biryani": 220},

             "dinner": {"noodles": 100,
                        "butter masala dosa": 120,
                        "idli sambhar": 80}}

# Global dictionaries and lists to store data
bookings = {}  
orders = []   
total_bill = {} 

# Flags to track if user has already used certain options
has_booked_room = False  
has_ordered_food = False 

# This keeps the program running until user exits
while True:
    print("\nchoose option")  # Clear line before showing menu
    
    # Show room booking option with status
    if not has_booked_room:
        print("1 - book a room")  
    else:
        print("1 - book another room") 
    
    # Show food ordering option with status  
    print("2 - order food")  
    
    # to Always show check and exit options
    print("3 - check existing bookings")
    print("4 - check food orders")
    print("5 - exit")

    # Getting user choice from main menu
    choice = input("enter 1, 2, 3, 4 or 5: ")

    # book a room, now for multiple rooms 
    if choice == '1':
        print("choose your room type - ")  
        for key, room in room_types.items():  
            print(f"{key} - {room['type']} (price of the room - {room['price']})")

        room_choice = input("select room type by number - ")  
        if room_choice not in room_types:
            print("invalid choice, try again.....")
            input("press enter to continue....") 
            continue 

        # customer details for booking
        print("enter details for booking - ")
        name = input("your name - ")
        age = input("your age - ")
        persons = input("no. of persons - ")
        date = input("date of booking - ")
        days = input("no. of days - ")

        
        if days.isdigit():  #to Check if days contains only numbers
            days_int = int(days)  # Converting to integer safely
        else:
            print("Please enter a valid number for days.")  
            input("press enter to continue....")
            continue  # back to the main menu

        # Generating unique random 3-digit room number
        while True:
            room_number = random.randint(100, 999)  
            if room_number not in bookings:  
                break  

        # Create booking information dictionary for this customer
        booking_info = {"name": name,
                        "age": age,
                        "persons": persons,
                        "date": date,
                        "days": days_int,
                        "food_orders": [],  # Empty list to store food orders for this room
                        "room_type": room_types[room_choice]["type"],
                        "room_price": room_types[room_choice]["price"]}

        # Store booking in main bookings dictionary
        bookings[room_number] = booking_info
        total_bill[room_number] = days_int * room_types[room_choice]["price"]  # Calculate room cost

        print(f"your room number {room_number} ({room_types[room_choice]['type']}) is booked")
        has_booked_room = True  

    # order food
    elif choice == '2':
        print("order food - enter your room number")
        room_number_input = input()  # Getting room number from customer

        
        if not room_number_input.isdigit():  # Check if contains only numbers
            print("Invalid room number format.")
            input("press enter to continue....")
            continue

        room_number_input = int(room_number_input)  # Convert to integer

        # Check if room exists in bookings
        if room_number_input not in bookings:
            print("room number not found - try again or please book a room first")
            input("press enter to continue....")
            continue

        # food ordering, Customer can order multiple items ANYTIME
        while True:
            print("\nchoose meal - ")  
            print("1 - breakfast")
            print("2 - lunch") 
            print("3 - dinner")
            print("0 - back to main menu") 
            
            meal_choice = input("enter 1,2,3 or 0: ")  

            # Allowing user to exit food ordering
            if meal_choice == '0':
                print("returning to main menu...")
                break  

            # breakfast ordering
            if meal_choice == '1':
                meal = "breakfast"
                print("breakfast menu - ")
                for key, item in food_menu[meal].items(): 
                    print(f"{key} - {item['name']} ({item['price']})")
                dish_choice = input("choose your dish by number: ")

                if dish_choice not in food_menu[meal]: 
                    print("invalid choice.... try again")
                    input("press enter to continue....")
                    continue

                dish = food_menu[meal][dish_choice]["name"]  
                price = food_menu[meal][dish_choice]["price"]  

            # lunch ordering
            elif meal_choice == '2':
                meal = "lunch"
                print("lunch menu - ")
                print("1 - rice with veg/non-veg curry")
                print("2 - naan bread with veg/non-veg curry")
                print("3 - biryani")

                dish_choice = input("choose your lunch 1,2 or 3: ")

                # Rice with curry 
                if dish_choice == '1':
                    base = "rice with "
                    print("choose your favourite curry - ")
                    print("1 - dal makhani")
                    print("2 - paneer butter masala")
                    print("3 - butter chicken")

                    curry_choice = input("choose your curry 1,2 or 3: ")

                    if curry_choice == '1':
                        curry = "daal makhani"
                    elif curry_choice == '2':
                        curry = "paneer butter masala"
                    elif curry_choice == '3':
                        curry = "butter chicken"
                    else:
                        print("invalid curry choice")
                        input("press enter to continue....")
                        continue

                    dish = f"{base}{curry}"
                    price = food_menu[meal].get(dish, 0)

                # Naan with curry
                elif dish_choice == '2':
                    base = "naan bread with "

                    print("choose your favourite curry")
                    print("1 - dal tadka")
                    print("2 - paneer tikka masala")
                    print("3 - lamb rogan josh")

                    curry_choice = input("choose your curry 1,2 or 3: ")

                    if curry_choice == '1':
                        curry = "dal tadka"
                    elif curry_choice == '2':
                        curry = "paneer tikka masala"
                    elif curry_choice == '3':
                        curry = "lamb rogan josh"
                    else:
                        print("invalid curry choice")
                        input("press enter to continue....")
                        continue

                    dish = f"{base}{curry}"
                    price = food_menu[meal].get(dish, 0)

                # Biryani choice
                elif dish_choice == '3':
                    base = "biryani"
                    print("choose veg or non-veg biryani - ")
                    print("1 - veg biryani")
                    print("2 - non-veg biryani")

                    biryani_choice = input("choose your biryani 1 or 2: ")

                    if biryani_choice == '1':
                        dish = "veg biryani"
                    elif biryani_choice == '2':
                        dish = "non-veg biryani"
                    else:
                        print("invalid biryani choice")
                        input("press enter to continue....")
                        continue

                    price = food_menu[meal].get(dish, 0)

                else:
                    print("invalid choice for lunch")
                    input("press enter to continue....")
                    continue

            # dinner order
            elif meal_choice == '3':
                meal = "dinner"
                print("dinner menu - ")

                for key, name in {"1": "noodles", "2": "butter masala dosa", "3": "idli sambhar"}.items():
                    print(f"{key} - {name} ({food_menu[meal][name]})")

                dish_choice = input("choose your dinner: ")

                if dish_choice not in ["1", "2", "3"]: 
                    print("invalid dinner choice")
                    input("press enter to continue....")
                    continue

                dish_names = {"1": "noodles", "2": "butter masala dosa", "3": "idli sambhar"}
                dish = dish_names[dish_choice]
                price = food_menu[meal][dish]

            # Invalid meal choice
            else:
                print("invalid meal choice, try again.")
                input("press enter to continue....")
                continue

            # Processing the food order
            orders.append(dish)  # Adding to orders list
            bookings[room_number_input]["food_orders"].append(dish)  # Add to room's food list

            # Updating total bill for this room
            if room_number_input in total_bill:
                total_bill[room_number_input] += price  # Add food price to existing bill
            else:
                total_bill[room_number_input] = price  # Create new bill

            print(f"your order for {dish} at price {price} has been placed")
            input("press enter to continue ordering or return to menu....")  # Pause after each order

        has_ordered_food = True

    # check bookings
    elif choice == '3':
        print("existing bookings - ")

        if bookings:  # Check if bookings exist
            for room_number, info in bookings.items():  
                print(f"room {room_number}: {info['room_type']}, name: {info['name']}, age: {info['age']}, persons: {info['persons']}, date: {info['date']}, days: {info['days']}")
                if info["food_orders"]:  
                    print(" food orders ")
                    for food in info["food_orders"]:
                        print(f" - {food}")
        else:
            print("no bookings found")

    # check all food orders
    elif choice == '4':
        print("all food orders")
        if orders:  
            for index, order_name in enumerate(orders, start=1): 
                print(f"{index}. {order_name}")
        else:
            print("no food orders found")

    # exit and pay the total bill
    elif choice == '5':
        print("lets settle your bills before you exit.....")
        if not bookings:
            print("you have no bookings or orders, thank you for cooperation")
            break  
        
        # Show all room bills
        total_sum = sum(total_bill.values())
        print(f"\nGRAND TOTAL for all rooms: {total_sum}")
        for room_number, total in total_bill.items():
            print(f"room {room_number} total bill (room + food): {total}")

        # payment check 
        while True:
            payment = input(f"please pay GRAND TOTAL {total_sum}: ")
            if payment.isdigit():  
                payment_amount = int(payment)  
                if payment_amount == total_sum: 
                    print("thank you for visiting the hotel, have a great day")
                    break 
                else:
                    print(f"paid amount does not match the GRAND TOTAL {total_sum} please pay the exact amount")
            else:
                print("Please enter a valid number.")

        break 

    else:
        print("invalid choice, choose from the options displayed")

    input("press enter to continue....")
