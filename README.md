# ATM Controller 

This is ATM Controller implemented by some of rules and my thoughts. 
First of all, `MockBankAPI` is implemented just for the unit-test and it provides 
account information based on card number and pin number. 
Then, the controller communicates with bank by `MocBankAPI` using card number and pin-number 
provided from the user. After thatn, the user can check the balance, deposit, and withdraw.
Every time the user use these services, the controller send the command to the bank and then, 
receive the account information. 

```
atm-controller/
├── controllers/
│   ├── __init__.py
│   └── base_controller/
│   └── controller.py
├── utils/
│   └── mock_bank_api.py
|
├── tests/
│   ├── __init__.py
│   └── test_atm_controller.py
├── setup.py
├── README.md
└── .gitignore
└── requirements.txt
```

- `BaseATMController` class is the base interface for the `ATMController` class. 
- `ATMController` is to communicate with bank by `bank_api`.
- `MockBankAPI` is implemented to unit-test `ATMController`.
- `test_atm_controller` is file to unit-test `ATMController` class.

### Install to develop or debug
```sh
python setup.py develop
```

### Run test
```sh
pytest .
```

