from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_data = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available: ")
            display_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < 0 or taxi_choice > len(taxis):
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[taxi_choice]
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill_data += trip_cost
        else:
            print("Invalid choice")
        print(f"Bill to date: ${bill_data:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${trip_cost:.2f}")
    print("Taxis are now:")
    display_taxi(taxis)

def display_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()