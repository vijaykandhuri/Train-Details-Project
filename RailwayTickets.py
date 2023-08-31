import random
class Account():
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def checkpassword(self,password):
      return self.password == password
    
class traininfo():
    def __init__(self,train_num,source,avl_seats,destination):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.avl_seats = avl_seats
        

    def displayinfo(self):
        print(35*"-")
        print(f"train_num:{self.train_num}")
        print(f"train_source : {self.source}")
        print(f"train_destination :{self.destination}")
        print(f"train_avl seats : {self.avl_seats}")
        print(35*"-")
                     
        
    def book_tickets(self, num_tickets):
        if tickets > self.avl_seats:
            return None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000, 999999))
            self.avl_seats -= tickets
            return pnr_list


class Passenger():
    def __init__(self,p_name,p_age,p_mobile_number,pnr_list):
        self.p_name = p_name
        self.p_age = p_age
        self.p_mobile_number = p_mobile_number
        self.pnr_list=pnr_list

    def  displayinfo(self):
        print("")
        print(f"passenger name:{self.p_name}")
        print(f"passenger age:{self.p_age}")
        print(f"passenger mobile number : {self.p_mobile_number}")       
        print("")


        
accounts = [
    Account("kumar", "2211")
]
loginaccount = None
while True:
    print("1.creat an account:\n2.login")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        username = input("enter name: ")
        password = input("enter password: ")
        accounts.append(Account(username,password))
        print("Account created succesfully")
    elif choice == 2:
        username = input("enter username: ")
        password = input("enter password: ")    
        for i in accounts:
            if i.username == username and i.checkpassword(password):
              loginaccount = i
              print(f"{username} Welcome to Train Booking ")

            break
        if loginaccount is None:
            print("invalid username and password")
        else:
            print("login successfull")
            break
    else:
        print("enter valid details")
#if loginaccount is not None:
trains =[traininfo(12345,"HYB",130,"Peddavaram"),
        traininfo(12255,"VZA",10,"Nandhigama"),
        traininfo(20701,"VANDHEBHARATH-SEC",155,"TPTY"),
        traininfo(12797,"VENKATADRI-KCG",76,"CTR"),
        traininfo(12734,"NARAYANADRI-LPI",54,"TPTY"),
        traininfo(12764,"PADMAVATHI-SEC",102,"TPTY"),
        traininfo(12797,"RAYALASEEMA-NZB",124,"TPTY"),
        traininfo(20834,"VANDHEBHARATH-SEC",50,"VSP")]



while True:
    user_input = input("Enter 1 to see Train Details , Enter 2 to Exit \n")
    if int(user_input) == 1:
        for train in trains:
           train.displayinfo()
        train_number = int(input("Enter Train Number:"))
        for i in range(len(trains)):
            if train_number == trains[i].train_num:
                print("Available tickets for this Train is:",trains[i].avl_seats)
                
                tickets = int(input("enter number of tickets to purchase:"))
                
                if  tickets <= trains[i].avl_seats:
                    while True:
                        try:
                            p_name = input("Enter passenger name:")
                            if not p_name:
                                raise ValueError("Name cannot be empty")
                            p_age  = int(input("Enter your age:"))
                            if p_age <= 0 or p_age > 120:
                                raise ValueError("Invalid Age")
                            p_mobile_number = input("enter your mobile number:")
                            if not p_mobile_number or len(p_mobile_number) != 10 or not p_mobile_number.isdigit():
                                raise ValueError("Invalid Phone Number")
                            
                            pnr_list = train.book_tickets(tickets)
                            #if pnr_list is not None:
                            print(35*"*")
                            print("Your PNR number is",pnr_list[0])
                            p = Passenger(p_name,p_age,p_mobile_number,pnr_list[0])
                            print(tickets,"Tickets have been booked")
                            p.displayinfo()
                            print(35*"*")
                            trains[i].avl_seats = trains[i].avl_seats-tickets
                            print(trains[i].avl_seats,"availble seats")
                            
                            print("Thanks for your Booking")
                            break
                        except ValueError as e:
                            print(f"Invalid Input: {e}")
                    
                else:
                    print("sufficient tickets are not avilable:")
                    break
                
    elif int(user_input) == 2:
        print("login again")
        break

    else:
        print("wrong details entered Re-enter again")
        

            


                    





         

          
