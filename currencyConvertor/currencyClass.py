"""" Name: Anthony Villalvazo-Cadena
Date: 12/1/23
Project: Currency Convertor Class
"""

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