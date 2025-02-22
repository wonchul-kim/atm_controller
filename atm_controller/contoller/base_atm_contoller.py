from typing import Optional
from abc import abstractmethod, ABC

class BaseATMController(ABC):
    def __init__(self, bank_api: Optional[str]):
        self.bank_api = bank_api
        self._connected_to_bank = False
        self._reset()
        
    @property 
    def bank_api(self):
        return self._bank_api

    @bank_api.setter 
    def bank_api(self, val):
        
        if val is not None:
            self.check_bank_api(val)
            
        self._bank_api = val
        
    @property 
    def inserted_card_number(self):
        return self._inserted_card_number

    @inserted_card_number.setter 
    def inserted_card_number(self, val):
        self._inserted_card_number = val
    
    @property 
    def inserted_card_account(self):
        return self._inserted_card_account
    
    @inserted_card_account.setter 
    def inserted_card_account(self, val):
        self._inserted_card_account = val
        
    @abstractmethod
    def insert_card(self, card_number: str) -> bool:
        self.inserted_card_number = card_number
    
    @abstractmethod
    def enter_pin_number(self, pin_number: str) -> bool:
        if not self._check_inserted_card_number():
            return False 
            
    @abstractmethod
    def select_account(self) -> bool:
        if not self._check_inserted_card_number():
            return False
        
    @abstractmethod
    def check_balance(self) -> Optional[int]:
        if not self._check_inserted_card_account() and self._connected_to_bank:
            return None 
    
    @abstractmethod
    def deposit(self, amount: int) -> bool:
        if not self._check_inserted_card_account() and self._connected_to_bank:
            return False 
    
    @abstractmethod
    def withdraw(self, amount: int) -> bool:
        if not self._check_inserted_card_account() and self._connected_to_bank:
            return False
    
    @abstractmethod
    def eject_card(self) -> bool:
        self._reset()
    
    def check_bank_api(self, val: str) -> bool:
        """
            I assume that there must be some function to check bank api
            including health check the communication with bank
        """

        # function_to_check_bank_api(val)
        # if it is true, 
        self._bank_api = val        
        self._connected_to_bank = True 
        
        return True 
        
    
    def _check_inserted_card_number(self) -> bool:
        if self._inserted_card_number:
            return True 
        else:
            return False
        
    def _check_inserted_card_account(self) -> bool:
        if self._inserted_card_account:
            return True 
        else:
            return False
        
    def _reset(self) -> None:
        self._inserted_card_number: Optional[str] = None 
        self._inserted_card_account: Optional[str] = None 