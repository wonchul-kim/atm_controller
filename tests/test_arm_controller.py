import unittest
from atm_controller.controllers import ATMController
from atm_controller.utils.mock_bank_api import MockBankAPI

class TestATMController(unittest.TestCase):
    def setUp(self):
        self.bank_api = MockBankAPI(bank_api_auth="1234qwer!")
        self.atm_controller = ATMController(self.bank_api)

    def test_insert_card(self):
        self.assertTrue(self.atm_controller.insert_card('1234 5678 1234 5678'))

    def test_enter_pin_number(self):
        self.atm_controller.insert_card("1234 5678 1234 5678")
        self.assertTrue(self.atm_controller.enter_pin_number("1234"))
        self.assertFalse(self.atm_controller.enter_pin_number("5678"))


    def test_check_balance(self):
        self.atm_controller.insert_card("1234 5678 1234 5678")
        self.atm_controller.enter_pin_number("1234")
        self.assertEqual(self.atm_controller.check_balance(), 1000)

    def test_deposit(self):
        self.atm_controller.insert_card("1234 5678 1234 5678")
        self.atm_controller.enter_pin_number("1234")
        self.assertTrue(self.atm_controller.deposit(500))
        self.assertEqual(self.atm_controller.check_balance(), 1500)

    def test_withdraw(self):
        self.atm_controller.insert_card("1234 5678 1234 5678")
        self.atm_controller.enter_pin_number("1234")
        self.assertTrue(self.atm_controller.withdraw(1000))
        self.assertEqual(self.atm_controller.check_balance(), 0)
        self.assertFalse(self.atm_controller.withdraw(5000))

    def test_eject_card(self):
        self.atm_controller.insert_card("1234 5678 1234 5678")
        self.atm_controller.enter_pin_number("1234")
        self.assertTrue(self.atm_controller.eject_card())
        self.assertIsNone(self.atm_controller.check_balance())

if __name__ == "__main__":
    unittest.main()
