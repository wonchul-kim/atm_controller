from typing import Optional
from abc import abstractmethod, ABC

class BaseATMController(ABC):
    def __init__(self, bank_api: Optional[str]):
        self.bank_api = bank_api
        self.check_bank_api()
        self._reset()
        
    @property 
    def bank_api(self):
        return self._bank_api

    @bank_api.setter 
    def bank_api(self, val):
        self._bank_api = val
        
    @property 
    def inserted_card_number(self):
        return self._inserted_card_number

    @inserted_card_number.setter 
    def inserted_card_number(self, val):
        self._inserted_card_number = val

    @property 
    def pin_number(self):
        return self._pin_number

    @pin_number.setter 
    def pin_number(self, val):
        self._pin_number = val
    
    @property 
    def inserted_card_account(self):
        return self._inserted_card_account
    
    @inserted_card_account.setter 
    def inserted_card_account(self, val):
        self._inserted_card_account = val
        
    @abstractmethod
    def insert_card(self, card_number: str) -> bool:
        self.inserted_card_number = card_number
    
    def check_pin_number(self, pin_number: str) -> bool:
        if not self._check_inserted_card_number():
            return False 
            
        if not self.bank_api.verify_pin_number(self.inserted_card_number, pin_number):
            return False 
        else:
            self.pin_number = pin_number
            return True
    
    def select_account(self) -> bool:
        if not self._check_inserted_card_number():
            return False
        
        self.inserted_card_account = self.bank_api.get_account(self.inserted_card_number)
        
        return self._check_inserted_card_account()
        
    @abstractmethod
    def check_balance(self) -> Optional[int]:
        pass
    
    @abstractmethod
    def deposit(self, amount: int) -> bool:
        pass
        
    @abstractmethod
    def withdraw(self, amount: int) -> bool:
        pass
        
    @abstractmethod
    def eject_card(self) -> bool:
        self._reset()
    
    @abstractmethod
    def check_bank_api(self) -> bool:
        pass
    
    def _check_inserted_card_number(self) -> bool:
        if self.inserted_card_number:
            return True 
        else:
            return False
        
    def _check_inserted_card_account(self) -> bool:
        if self.inserted_card_account:
            return True 
        else:
            return False
        
    def _reset(self) -> None:
        self.inserted_card_number: Optional[str] = None 
        self.pin_number: Optional[str] = None 
        self.inserted_card_account: Optional[str] = None 