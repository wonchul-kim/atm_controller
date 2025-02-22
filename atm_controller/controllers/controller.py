from typing import Optional
from atm_controller.controllers import BaseATMController

class ATMController(BaseATMController):
    def __init__(self, bank_api: Optional[str]):
        super().__init__(bank_api=bank_api)
    
    def check_bank_api(self) -> bool:
        # TODO: I assume that there must be something like to check api health
        # now it is true as default
        
        return True     
    
    def insert_card(self, card_number: str) -> bool:
        super().insert_card(card_number)
        
        return True 
    
    def enter_pin_number(self, pin_number: str) -> bool:
        if not self.check_pin_number(pin_number) or not self.select_account():
            return False
        
        return True
           
    def check_balance(self) -> Optional[int]:
        if not self._check_inserted_card_account():
            return None 
        else:
            return self.inserted_card_account['balance']
    
    def deposit(self, amount: int) -> bool:
        if not self._check_inserted_card_account():
            return False
        
        if self.bank_api.deposit(self.inserted_card_number, 
                                     self.pin_number,
                                     amount):
            self.select_account()
            return True 
        else:
            return False
    
    def withdraw(self, amount: int) -> bool:
        if not self._check_inserted_card_account():
            return False
        
        # if there is no momey, disable withdraw
        if self.inserted_card_account['balance'] < amount:
            return False
        
        if self.bank_api.withdraw(self.inserted_card_number, 
                                      self.pin_number,
                                      amount):
            self.select_account()
            return True 
        else:
            return False
    
    def eject_card(self) -> bool:
        super().eject_card()
        
        return True
    
from atm_controller.utils.mock_bank_api import MockBankAPI
atm_controller = ATMController(MockBankAPI("1234qwer!"))
atm_controller.insert_card('1234 5678 1234 5678')
atm_controller.enter_pin_number('1234')
atm_controller.enter_pin_number('45')
print(atm_controller.inserted_card_account)
print(atm_controller.check_balance())
print(atm_controller.deposit(12), atm_controller.inserted_card_account)
print(atm_controller.withdraw(13), atm_controller.inserted_card_account)
print(atm_controller.eject_card(), atm_controller.inserted_card_account)
atm_controller.check_balance()