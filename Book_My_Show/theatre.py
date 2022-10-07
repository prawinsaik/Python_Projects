from textwrap import indent
from pprint import pprint
import sys


class Theatre:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.seats = [["S" for j in range(cols)] for i in range(rows)]
        self.booked_ticket = {}
        self.set_ticket_price()
        self.tickets_count = 0

        self.total_income = 0

    def show_seats(self):
        print('\t\tCinema: ')
        # print('\t\t','*'*30)
        print('*'*100)
        print('\t\t', end=' ')
        for i in range(self.cols+1):
            if i != 0:
                print(i, end='  ')
            else:
                print(" ",end = '  ')
        print()

        for i in range(self.rows):
            print('\t\t', i+1, end='  ')
            for j in range(self.cols):
                print(self.seats[i][j], end='  ')
            print()
        # print('\t\t','*'*30)
        print('*'*100)

    def set_ticket_price(self):
        total_number_of_seats = self.rows * self.cols

        if total_number_of_seats < 60:
            self.front_half = 10.00
            self.back_half = 10.00

        else:
            self.front_half = 10.00
            self.back_half = 8.00

    def book_ticket(self):
        row, column = map(int, input("Enter the row and column: ").split())
        ticket_price = 0

        #check if ticket is booked already
        if self.seats[row-1][column-1] == 'B':
            print('Ticket already booked...!')

        elif self.seats[row-1][column-1] == 'S':
            if row < int(self.rows/2):
                ticket_price = self.front_half

            else:
                ticket_price = self.back_half

            #updating the income
            self.total_income += ticket_price

            print("Ticket price: Rs.", ticket_price, ",Do you want to continue booking: ")
            display = '1.Yes,\n2.No:'
            print(display)
            choice = int(input("Enter the number: "))
            if choice == 1:
                name = input("ENTER NAME: ")
                gender = input("ENTER GENDER: ")
                age = int(input("ENTER AGE: "))
                phone_number = input("ENTER PHONE NUMBER: ")

                user_details = {'name':name, 'gender':gender, 'age':age, 'phone_number':phone_number}
                
                key = "{}_{}".format(row,column)
                self.booked_ticket[key] = user_details
                
                #changing ticket status
                self.seats[row-1][column-1] ='B'

                #increasing the ticket count
                self.tickets_count += 1

            print('TICKET BOOKED SUCCESSFULLY....!')
            
        else:
            print('SEAT NOT PRESENT...!')

    def statistics(self):
        display = '1. Number of Purchased Tickets,\n2. Percentage of Tickets booked,\n3. Current Income,\n4. Total Income.'
        print('\nSTATISTICS')
        print(display)

        user_choice = int(input("Enter your choice: "))
        
        if user_choice == 1:
            print('Total Number of Tickets purchased: ', self.tickets_count)


        elif user_choice == 2:
            total_seats = self.rows * self.cols
            percentage_of_tickets_booked = ((self.tickets_count/total_seats)*100)
            
            print("Booking Percentage: {0:.2f} %".format(percentage_of_tickets_booked))

        elif user_choice == 3:
            print("Current Income: Rs.", self.total_income)

        elif user_choice == 4:
            print("Total Income: Rs.", self.total_income)

    
    def show_booked_user_info(self):
        row, column = map(int, input("Enter the row and column: ").split())

        #check if ticket is booked already
        if self.seats[row-1][column-1] == 'B':
            key = '{}_{}'.format(row,column)
            # pprint(self.booked_ticket)
            user_dict = self.booked_ticket[key]
            print("\nUser Details: ")
            # pprint(user_dict)

            for k,v in user_dict.items():
                print('\t\t',k.capitalize(),' : ', v)
                # print()

        elif self.seats[row-1][column-1] == 'S':
            print("SEAT NOT BOOKED")