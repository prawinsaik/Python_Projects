from theatre import Theatre
# from theatre import *

print("\t\t"+"*"*10 + "WELCOME" + "*"*10)

def get_user_input():
    rows, columns = map(int, input("Enter the number of rows and columns seperated by space: ").split())    
    theatre = Theatre(rows, columns)

    display = "\n1. Show the seats,\n2. Buy a ticket,\n3. Statistics,\n4. Show booked Tickets User info,\n0. Exit"

    show_menu = True

    while show_menu:
    
        print(display)
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            #show tickets
            theatre.show_seats()

        elif user_choice == 2:
            #buy a ticket
            theatre.book_ticket()

        elif user_choice == 3:
            #statistics
            theatre.statistics()

        elif user_choice == 4:
            #show booked ticket user info
            theatre.show_booked_user_info()

        elif user_choice == 0:
            print("Exit")
            break

        else:
            print("Invalid Choice...!")
        
def main():
    pass 

if __name__ == '__main__':
    get_user_input()