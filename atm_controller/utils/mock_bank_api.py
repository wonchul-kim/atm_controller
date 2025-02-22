from typing import Optional, Dict, Union

class MockBankAPI:
    """
        Just assume that the bank works as the below
    """
    def __init__(self, bank_api_auth: str):
        
        # Need to check bank_api_auth 
        
        # Account DataBase
        self.accounts: Dict[str, Dict[str, Union[str, int]]] = {
                "1234 5678 1234 5678": {
                    "pin_number": "1234",
                    "account": {
                                "balance": 1000,
                    }
                }
            }

    def verify_pin_number(self, card_number: str, pin_number: str) -> bool:
        return card_number in self.accounts and self.accounts[card_number]["pin_number"] == pin_number

    def get_account(self, card_number: str) -> Optional[str]:
        if card_number in self.accounts:
            return self.accounts[card_number]['account']
        
        return None

    def deposit(self, card_number: str, pin_number: str, amount: int) -> bool:
        if self.verify_pin_number(card_number, pin_number):
            self.accounts[card_number]['account']['balance'] += amount
            return True
        else:
            return False

    def withdraw(self, card_number: str, pin_number: str, amount: int) -> bool:
        if self.verify_pin_number(card_number, pin_number):
            self.accounts[card_number]['account']['balance'] -= amount
            return True
        else:
            return False