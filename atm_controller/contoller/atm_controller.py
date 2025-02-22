from typing import Optional, Union
from base_atm_contoller import BaseATMController

class ATMController(BaseATMController):
    def __init__(self, bank_api: str):
        super().__init__(bank_api)
    
    def insert_card(self, card_number: str) -> bool:
        super().insert_card(card_number)
        
        return True 
    
    def enter_pin_number(self, pin_number: str) -> bool:
        super().enter_pin_number(pin_number)

        return self.bank_api.verify_pin_number(self.inserted_card_number, pin_number)
    
    def select_account(self) -> bool:
        super().select_account()
        
        self.inserted_card_account = self.bank_api.get_account(self.inserted_card_number)
        
        return self._check_inserted_card_account()
        
    def check_balance(self) -> Optional[int]:
        super().check_balance()
        
        return self.bank_api.get_balance(self.inserted_card_account)
    
    def deposit(self, amount: int) -> bool:
        super().deposit(amount)
        
        return self.bank_api.deposit(self.inserted_card_account, amount)
    
    def withdraw(self, amount: int) -> bool:
        super().withdraw(amount)
        
        return self.bank_api.withdraw(self.inserted_card_account, amount)
    
    def eject_card(self) -> bool:
        super().eject_card()
        
        return True
    
controller = ATMController(bank_api='abc')
controller.insert_card('abc')