# PROGRAM HEADER
"""" Name: Anthony Villalvazo-Cadena
Date: 9/27/23 --- Part A
      10/26/23 --- Part B
      11/27/23 --- Part C
Assignment: Semester Project - Currency Converter
"""

# PSEUDOCODE
""" 
Goal:
        The project goal is to create a currency converter with all the major currencies. It will ask you what currency 
        you have, and then to what currency you want to convert to. For this program, because I live in the use, I will
        be using USD as the base currency for all my conversions. 
    
"""

from collections import deque
import json

### CLASSES ###

# MAIN CLASS OF CURRENCY
class Currency():
    '''Description: This class is to model the object of currency
            Attributes:
                name (str): contains the name of currency
                code (str): contains the code of the currency (USD, EUR)
                symbol(str): contatins the symbol of the currency ($)
            Behaviors:
                nothing
    '''
    # ATTRIBUTES
    _name = ""
    _code = ""
    _symbol = ""

    # CONSTRUCTOR
    def __init__(self, name, code, symbol):
        self._name = name
        self._code = code
        self._symbol = symbol

    # SETTERS - ONLY FOR ADMIN USE
    def setName(self, name):
        self._name = name

    def setCode(self, code):
        self._code = code

    def setSymbol(self, symbol):
        self._symbol = symbol

    # GETTERS - USED BY USER/ADMIN
    def getName(self):
        return self._name

    def getCode(self):
        return self._code

    def getSymbol(self):
        return self._symbol


# SUBCLASS 1 - FIATCURRENCY
class FiatCurrency(Currency):
    '''Description: This subclass is to model the object of Fiatcurrency (state currency)
                Attributes:
                    exchange rate (str): contains the exchange rate of the currency
                    origin (str): contains the origin state of the currency
                Behaviors:
                    nothing
        '''
    _rate = ""
    _origin = ""

    # CONSTRUCTOR
    def __init__(self, name, code, symbol, rate:float , origin):
        # USING METHODS/ATTRIBUTES FROM BASE CLASS
        super().__init__(name, code, symbol)
        self._rate = rate
        self._origin = origin

    # SETTERS - FOR ADMIN
    def setRate(self, rate):
        self._rate = rate

    def setOrigin(self, origin):
        self._origin = origin

    # GETTERS - FOR ADMIN/USER
    def getRate(self):
        return self._rate

    def getOrigin(self):
        return self._origin

    # BEHAIVIOR - USER/ADMIN
    def convertFiat(self, user_input:float, currency):
        '''Description: This behavior is designed to convert to fiat currencies. It will show how much
           a certain fiat is in relation to their currency of choice. This can be either Fiat or Crypto.
                Parameters:
                    user_input (str): contains the choice of their currency that they have
                    currency (str): This contains the fiat currency they want to convert to
                Return:
                    value: (int) This will show the value of the converted currency from user_input -> currency
        '''

        conversion = user_input * self._rate
        return conversion

    #PRINT METHOD THAT WILL PRINT THE NAME OF THE SYMBOL ONCE IT'S CALLED
    def __str__(self):
        return self._code




# SUBCLASS 2 - CRYPTOCURRENCY
class CryptoCurrency(Currency):
    '''Description: This subclass is to model the object of Crypto currency (online encrypted currency)
                    Attributes:
                        blockchain technology (str): contains the block chain technology the coin uses
                        price (int): contains the price of the coin (USD)
                    Behaviors:
                        nothing
            '''
    _blckchain_tech = ""  # TECHNOLOGY ON WHICH THE CRYPTOCURRENCY IS BASED
    _rate_cc = 0  # PRICE AS IT RELATES TO USD

    def __init__(self, name, code, symbol, tech, rate:float):
        # USING METHODS/ATTRIBUTE FROM BASE CLASS
        super().__init__(name, code, symbol)
        self._blckchain_tech = tech
        self._rate_cc = rate

    # SETTERS - FOR ADMIN
    def setTech(self, tech):
        self._blckchain_tech = tech

    def setRate(self, rate:float):
        self._rate_cc = rate

    # GETTERS - FOR ADMIN/USER
    def getTech(self):
        return self._blckchain_tech

    def getRate(self):
        return self._rate_cc

    # BEHAIVOR - USER/ADMIN
    def convertCrypto(self, user_input:float, currency):
        '''Description: This behavior is designed to convert to cryptocurrencies. It will show how much
           a certain cryptocurrency is in relation to their currency of choice. This can be either Fiat or Crypto.
                Parameters:
                    user_input (str): contains the choice of their currency that they have
                    currency (str): This contains the crypto currency they want to convert to
                Return:
                    value: (int) This will show the value of the converted currency from user_input -> currency
        '''

        conversion = user_input *  self._rate_cc
        return conversion

    #PRINT METHOD THAT WILL PRINT THE NAME OF THE SYMBOL ONCE IT'S CALLED
    def __str__(self):
        return self._code


#### MAIN PROGRAM INTERFACE ####

#Here I am creating default instances for each of the currencies, I would do a loop but i have to individually input different attributes for each currency
#for all the rates, the exchange rate will be USD to Desired currency for easy calculations

#CYRPTO INSTANCES
bitcoin=CryptoCurrency("Bitcoin", "BTC", "₿", "Bitcoin blockchain", 0.0000270005 )
dogecoin=CryptoCurrency("Dogecoin", "DOGE", "Ð", "Dogecoin blockchain", 12.6164695143 )
ethereum=CryptoCurrency("Ethereum", "ETH", "Ξ", "Ethereum blockchain", 0.0005012204 )
litecoin=CryptoCurrency("Litecoin", "LTC", "Ł", "Litecoin blockchain", 0.0145887819 )

#FIAT INSTANCES
yuan=FiatCurrency("Chinese Yuan Renminbi", "CNY", "¥", 7.1235471, "China")
euro=FiatCurrency("Euro", "EUR", "€", 0.91295791, "European Union")
yen=FiatCurrency("Japanese Yen", "JPY", "¥", 148.60706, "Japan")
us_dollar=FiatCurrency("US Dollar", "USD", "$", 1.00, "United States of America")

#PUTTING THE INSTANCES IN A DICITONARY FOR MENU OPTIONS
crypto = {1: bitcoin, 2: dogecoin, 3: ethereum, 4: litecoin}
fiat = {1: yuan, 2: euro, 3: yen, 4: us_dollar}


#THESE ARE THE DICTIONARIES THAT WILL BE SENT TO A PERMENANT JSON FILE
admin_history={


}

user_history={

}

convertor_history = { "User History": user_history, "Admin History": admin_history

}


"MENU INTERFACE - ASKS FOR USER OR ADMIN"

# this loop asks user if they are user or an admin
# if they don't choose either an A or a U, then an error will occur and will ask to input again

while True:

    print("Welcome to Anthony's Currency Convertor. Would you like to continue or exit the program?")
    exit_choice = input("Please Enter 'C' to continue or 'E' to exit: " )
    if exit_choice == "C" or exit_choice == "c":

        while True:
            user = input("Please type 'U' for user or 'A' for admin: ")
            if user in ['a', 'A', 'u', 'U']:
                break
            else:
                print('Please Enter a valid value!')


        # ---------------------------FOR ADMIN---------------------------------
        password = "ADMIN"

        # if user is Admin, it will ask to enter a password to log in,else, it will give the user normal user options
        if user == 'a' or user == 'A':
            #Once the user picks a or A, an admin stack is created for later use
            admin_stack =[]
            admin_name = input("Please enter your name: ")
            admin_stack.append(admin_name)


            while True:
                password_input = input(f"Welcome {admin_name}. Please Enter Password: ")
                if password_input != password:
                    print("Incorrect Password. Please try again!")
                else:
                    break

            # This section is setting a dictionary data type to the variable for later use
            type_currency = {1: "Update Crypto Currency", 2: "Update FiatCurrency", 3: "Print History"}
            print("These are the available options: ")



            # MENU LOOP FOR ADMIN
            # If the choice is out of range or if the choice is not an integer value, they will recieve corresponiding error messages
            while True:
                try:
                    # This will display the menu choice for type of currency
                    for i in type_currency:
                        print(f"{i}. {type_currency[i]}")
                    choice = int(input("Please select one of the options: "))
                    if choice in type_currency:
                        print(f"You have chosen {type_currency[choice]}")
                        admin_stack.append(type_currency[choice])    #appending the type of currecny they chose
                        break
                    # used when admin enters a value outside of the range of the dictionary key
                    else:
                        print("Please enter a valid choice within the given range!")
                # value error used when admin enters anything other than int
                except ValueError:
                    print("Please enter an integer value!")



            # This loop will ask which speficic currency the admin want to work on within the crypto/fiat category
            while True:

                # This try loop will prevent error if they try to choose a string
                try:

                    # this if statement is for cyrpto. Will ask user which crypto coin they want to use. Has error handling within the statement.
                    if choice == 1:
                        for i in crypto:
                            print(f"{i}. {crypto[i]}")

                        crypto_choice = int(input("Please select the Crypto Currency you want to work on: "))
                        if crypto_choice in crypto:
                            print(f"You have chosen {crypto[crypto_choice]}")
                            coin = crypto[crypto_choice]
                            admin_stack.append(coin.getCode())  #appending the crytpo choice to the stack



                            #----------------------------ADMIN CONTROLS FOR CRYPTO ac = admin crypto------------------------------------
                            #MAKING A QUEUE FROM DEQUE PACKAGE IN PYTHON
                            #I WILL USE A QUEUE SO HOLD THE CURRENCY THEY HAVE, AND THE CHANGES THEY WANT TO MAKE TO IT
                            ac_queue=deque()
                            ac_queue.append(coin)
                            #MENU DICTIONARY FOR THE CRYPTO CONTROLS
                            crypto_controls={1: "Set Blockchain Tech", 2 :"Set Exchange Rate", 3: "Retrieve Blockchain Tech", 4: "Retrieve Exchange Rate"}
                            while True:
                                try:
                                    for i in crypto_controls:
                                        print(f"{i}. {crypto_controls[i]}")
                                    crypto_control_choice = int(input("Please select the change you wish to make: "))

                                    if crypto_control_choice in crypto_controls:
                                        print(f"You have chosen {crypto_controls[crypto_control_choice]}")
                                        admin_stack.append(crypto_controls[crypto_control_choice])


                                        #CONDITIONALS WILL DECIDE WHICH METHOD TO RUN BASED ON INPUT

                                        #THIS SETS THE NEW BLOCKCHAIN TECHNOLOGY
                                        if crypto_control_choice==1:
                                            new_tech=input("Please enter the new blockchain technology: ")
                                            ac_queue.append(new_tech)
                                            coin=ac_queue.popleft()
                                            coin.setTech(ac_queue.popleft())
                                            admin_stack.append(new_tech)
                                            print(f"Success, the new technology is {coin.getTech()}")


                                        #THIS SETS THE EXCHANGE RATE
                                        if crypto_control_choice==2:
                                            # this loop makes sure the input is a float
                                            while True:
                                                new_rate=float(input("Please Enter a decimal value for rate: "))
                                                if isinstance(new_rate, float):
                                                    ac_queue.append(new_rate)
                                                    coin=ac_queue.popleft()
                                                    coin.setRate(ac_queue.popleft())
                                                    admin_stack.append(new_rate)
                                                    print(f"Success, the new rate is {coin.getRate()}")
                                                    break
                                                else:
                                                    print("Please enter a decimal value and try again!")

                                        #THIS RETRIEVES THE BLOCKCHAIN TECH
                                        if crypto_control_choice==3:
                                            coin=ac_queue.popleft()
                                            print(f"The blockchain tech is {coin.getTech()}")


                                        #THIS GETS THE EXCHANGE RATE
                                        if crypto_control_choice==4:
                                            coin = ac_queue.popleft()
                                            print(f"The exchange rate is {coin.getRate()}")


                                        #ADD THE INFO FROM THE STACK TO THE HISTORY HERE
                                        print(admin_stack)


                                        break
                                    else:
                                        print("Please enter a valid choice within the given range!")
                                except ValueError:
                                    print("Please enter an integer!")


                            break
                        else:
                            print("Please enter a valid choice within the given range!")
                        #ENDING OF ADMIN CONTROLS FOR CRYPTO


                    # This else statement is for fiat. Will ask user whih fiat currency they want to use. Has error handling within it.
                    if choice==2:
                        for i in fiat:
                            print(f"{i}. {fiat[i]}")
                        fiat_choice = int(input("Please select the Fiat currency you want to work on: "))
                        if fiat_choice in fiat:
                            print(f"You have chosen {fiat[fiat_choice]}")
                            money=fiat[fiat_choice]
                            admin_stack.append(money.getCode())



                            #----------------------------ADMIN CONTROLS FOR FIAT af = admin fiat------------------------------------
                            # MAKING A QUEUE FROM DEQUE PACKAGE IN PYTHON
                            # I WILL USE A QUEUE SO HOLD THE CURRENCY THEY HAVE, AND WHAT CHANGES THEY WANT TO MAKE TO IT
                            af_queue = deque()
                            af_queue.append(money)

                            # MENU DICTIONARY FOR THE FIAT CONTROLS
                            fiat_controls = {1: "Set Country of Origin", 2: "Set Exchange Rate", 3: "Retrieve Origin", 4: "Retrieve Exchange Rate"}
                            while True:
                                try:
                                    for i in fiat_controls:
                                        print(f"{i}. {fiat_controls[i]}")
                                    fiat_control_choice = int(input("Please select the change you wish to make: "))

                                    if fiat_control_choice in fiat_controls:
                                        print(f"You have chosen {fiat_controls[fiat_control_choice]}")
                                        admin_stack.append(fiat_controls[fiat_control_choice])

                                        # CONDITIONALS WILL DECIDE WHICH METHOD TO RUN BASED ON INPUT

                                        # THIS SETS THE NEW PLACE OF ORIGIN
                                        if fiat_control_choice == 1:
                                            new_origin = input("Please enter the new Country/Region of Origin: ")
                                            af_queue.append(new_origin)
                                            money = af_queue.popleft()
                                            money.setOrigin(af_queue.popleft())
                                            admin_stack.append(new_origin)
                                            print(f"Success, the new place of origin is {money.getOrigin()}")

                                        # THIS SETS THE EXCHANGE RATE
                                        if fiat_control_choice == 2:
                                            # this loop makes sure the input is a float
                                            while True:
                                                new_rate = float(input("Please Enter a decimal value for rate: "))
                                                if isinstance(new_rate, float):
                                                    af_queue.append(new_rate)
                                                    money = af_queue.popleft()
                                                    money.setRate(af_queue.popleft())
                                                    admin_stack.append(new_rate)
                                                    print(f"Success, the new rate is {money.getRate()}")
                                                    break
                                                else:
                                                    print("Please enter a decimal value and try again!")

                                        # THIS RETRIEVES THE ORIGIN
                                        if fiat_control_choice == 3:
                                            money = af_queue.popleft()
                                            print(f"The place of origin is: {money.getOrigin()}")

                                        # THIS GETS THE EXCHANGE RATE
                                        if fiat_control_choice == 4:
                                            money = af_queue.popleft()
                                            print(f"The exchange rate is {money.getRate()}")

                                        # ADD THE INFO FROM THE STACK TO THE HISTORY HERE
                                        print(admin_stack)






                                        break
                                    else:
                                        print("Please enter a valid choice within the given range!")
                                except ValueError:
                                    print("Please enter an integer!")



                            break
                        else:
                            print("Please enter a valid choice within the given range!")
                        #ENDING OF ADMIN CONTROLS FOR FIAT

                    #OPTION FOR IF PRINT HISTORY IS CHOSEN
                    if choice==3:
                        #INSERT PROGRAM IF PRINT HISOTRY IS CHOSEN (REALLY SHORT)
                        try:
                            file_path = "convertor_history.json"
                            with open(file_path, "r") as json_file:
                                history=json.load(json_file)

                            if admin_name in history:
                                admin_info=history[admin_name]
                                print(f"Information for {admin_name}: ")
                                print(admin_info)
                                break

                            else:
                                print("User Not Found!")
                                break
                        except:
                            print("Please go through the program first, then you can see convertor history!")
                            break




                except ValueError:
                    print("Please enter an integer value!")
        #ENDING OF ADMIN SECTION
            #THIS SECTION WILL WRITE ADMIN HISOTRY INTO NEW JSON FILE
            if len(admin_stack)>0:
                admin_stack.reverse()
                admin_dict= {}
                admin_stack_copy = admin_stack[:]
                admin_dict["Name"]=admin_stack.pop()
                # THIS ADDS THE ROLE OF THIS USER
                admin_dict["ROLE"] = "ADMIN"

                #THIS LOOP WILL LOOP THROUGH WITH THE LENGTH OF THE STACK WITHOUT THE NAME AS THE CONDITION
                i=1
                while i<len(admin_stack_copy):
                    admin_dict[f"Input {i}"]=admin_stack.pop()
                    i+=1
                admin_history[admin_name] = admin_dict


                #THIS IS THE PART WHERE I WILL WRITE INFO TO JSON FILE
                file_path = "convertor_history.json"
                with open(file_path, "w") as json_file:
                    json.dump(admin_history, json_file, indent=4)




        # ---------------------- FOR USER ------------------------
        # If user is a normal user, it will create them a menu selection to start the currency conversion

        else:
            # making a dictionary that shows all the currency we have to choose from
            currency = {1: "Convert Fiat Currency", 2: "Convert Crypto Currency", 3:"Print History"}
            user_name = input("Please enter your name: ")
            user_stack = []
            user_stack.append(user_name)


            print("Welcome to Anthony's Currency Convertor")
            print("These are the available options")



            # MENU LOOP FOR USER

            while True:
                # The try block will repeat until the user finally chooses something within the range of the dictionary --- The currencies
                try:
                    # This loop shows the user the 5 available currencies
                    for i in currency:
                        print(f"{i}. {currency[i]}")


                    choice = int(input("Please Select an option: "))
                    if choice in currency:
                        print(f"You have chosen: {currency[choice]}")
                        user_stack.append(currency[choice])



                        #IF THEY CHOSE FIAT
                        if choice ==1:
                            while True:
                                try:
                                    for i in fiat:
                                        print(f"{i}. {fiat[i]}")
                                    fiat_choice = int(input("Please select the Fiat currency you are starting with: "))

                                    if fiat_choice in fiat:
                                        print(f"You have chosen {fiat[fiat_choice]}")
                                        starting=fiat[fiat_choice]
                                        user_stack.append(starting.getCode())

                                        #THIS LOOP WILL KEEP ASKING USER TO ENTER HOW MUCH THEY HAVE OF CHOSEN CURRENCY UNTIL THEY PUT IN AN INTEGER VALUE
                                        while True:
                                            try:
                                                amount = float(input("Please type a numerical value to show the amount you have of the original currency: "))
                                                break
                                            except:
                                                print("Please enter a valid value!")

                                        #THIS SMALL CALCULATION CONVERTS STARTING CURRENCY TO USD FOR LATER USE
                                        amount_in_usd = amount * (1/starting.getRate())


                                        #----------------------------USER CONVERSIONS FOR FIAT uf = user fiat------------------------------------
                                        #I WILL USE QUEUE TO STORE WHICH CURRENCY THE USER HAS, AND WHICH THEY WANT TO CONVERT TO
                                        uf_queue= deque()
                                        uf_queue.append(starting)
                                        #INSERT MAIN USER CONVERSION IN HERE

                                        #THis LOOP WILL ASK FOR WHICH CURRENCY THE USER WANTS TO CONVERT TO

                                        for i in fiat:
                                            print(f"{i}. {fiat[i]}")
                                        end_choice=int(input("Please select the Fiat currency you want to convert to: "))

                                        if end_choice in fiat:
                                            print(f"You have chosen {fiat[end_choice]}")
                                            ending=fiat[end_choice]
                                            uf_queue.append(ending)
                                            user_stack.append(ending.getCode())
                                            final_value = amount_in_usd * ending.getRate()
                                            print(f"{uf_queue.popleft().getSymbol()}{amount} is approximately {uf_queue.popleft().getSymbol()}{final_value:.2f}")
                                            break
                                        else:
                                            print("Please enter a valid choice within the given range!")




                                    else:
                                        print("Please enter a valid choice within the given range!")
                                except ValueError:
                                    print("Please Enter Integer!")
                            break
                            #ENDING OF USER FIAT CONTROLS


                        #IF THEY CHOSE CRYTPO CURRENCY
                        if choice==2:
                            # This loop block will loop through the crypto coins if the user chooses option 2
                            while True:
                                try:

                                    if choice == 2:
                                        for i in crypto:
                                            print(f"{i}. {crypto[i]}")
                                        user_crypto_choice = int(input("Please select the Crypto Currency you are starting with: "))
                                       # This if and else pair is small error handling for if the user chooses a number out of range
                                        if user_crypto_choice in crypto:
                                            print(f"You have chosen {crypto[user_crypto_choice]}")
                                            starting=crypto[user_crypto_choice]
                                            while True:
                                                try:
                                                    amount = float(input("Please type a numerical value to show the amount you have of the original currency: "))
                                                    user_stack.append(amount)
                                                    break
                                                except:
                                                    print("Please enter a valid value!")
                                            # THIS SMALL CALCULATION CONVERTS STARTING CURRENCY TO USD FOR LATER USE
                                            amount_in_usd = amount * (1 / starting.getRate())


                                            #----------------------------USER CONVERSIONS FOR CRYPTO uc = user crypto------------------------------------
                                            # I WILL USE QUEUE TO STORE WHICH CURRENCY THE USER HAS, AND WHICH THEY WANT TO CONVERT TO
                                            uc_queue = deque()
                                            uc_queue.append(starting)
                                            #INSERT MAIN USER CONVERSION IN HERE



                                            #TTHIS WILL ASK THE USER WHICH CURRENCY THEY WANT TO CONVERT TO AND PRINT THE RESULTS
                                            for i in crypto:
                                                print(f"{i}. {crypto[i]}")
                                            end_choice = int(input("Please select the cryptocurrency you want to convert to: "))

                                            if end_choice in crypto:
                                                print(f"You have chosen {crypto[end_choice]}")
                                                ending = crypto[end_choice]
                                                uc_queue.append(ending)
                                                user_stack.append(ending.getCode())
                                                final_value = amount_in_usd * ending.getRate()
                                                print(f"{uc_queue.popleft().getSymbol()}{amount} is approximately {uc_queue.popleft().getSymbol()}{final_value:.2f}")
                                                break
                                            else:
                                                print("Please enter a valid choice within the given range!")

                                            break





                                        else:
                                            print("Please enter a valid choice within the given range!")
                                except ValueError:
                                    print("Please enter an integer value.")
                            break
                            #ENDING OF USER CYRPTO CONTORLS

                        #THIS SECTION IS IF THEY CHOOSE 3 - PRINT HISTORY
                        if choice==3:
                            # INSERT PROGRAM IF PRINT HISOTRY IS CHOSEN (REALLY SHORT)
                            try:
                                file_path = "convertor_history.json"
                                with open(file_path, "r") as json_file:
                                    history = json.load(json_file)

                                if user_name in history:
                                    user_info = history[user_name]
                                    print(f"Information for {user_name}: ")
                                    print(user_info)
                                    break

                                else:
                                    print("User Not Found.!")
                                    break
                            except:
                                print("Please go through the program first, then you can see convertor history!")
                                break



                    else:  # used when user enters a value outside of the range of the dictionary key
                        print("Please enter a valid choice within the given range!")
                except ValueError:  # value error used when user enters anything other than int
                    print("Please enter an integer value.")
            #END OF USER SECTION


            if len(user_stack) > 0:
                user_stack.reverse()
                user_dict = {}
                user_stack_copy = user_stack[:]
                user_dict["Name"] = user_stack.pop()
                # THIS ADDS THE ROLE OF THIS USER
                user_dict["ROLE"] = "USER"

                # THIS LOOP WILL LOOP THROUGH WITH THE LENGTH OF THE STACK WITHOUT THE NAME AS THE CONDITION
                i = 1
                while i < len(user_stack_copy):
                    user_dict[f"Input {i}"] = user_stack.pop()
                    i += 1
                user_history[user_name] = user_dict

                file_path = "convertor_history.json"
                with open(file_path, "w") as json_file:
                    json.dump(user_history, json_file, indent=4)



    elif exit_choice=="E" or exit_choice=="e":
        print("Thank you for choosing Anthony's Currency Convertor.")
        break
    else:
        print("Please Enter a valid value!")
