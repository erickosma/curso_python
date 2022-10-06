import unittest

from src.account import Account


class AccountTestCase(unittest.TestCase):

    def test_account(self):
        account = Account(123, "Eu Ddono", 55.5, 1000.0)
        self.assertEqual(123, account.number)

    def test_account_transfer(self):
        nico_account = Account(123, "Nico", 55.5, 1000.0)
        marcos_account = Account(321, "Marcos", 100.0, 1000.0)

        nico_account.transfer(10.0, marcos_account)
        self.assertEqual("Saldo de 45.5 do titular Nico", nico_account.statement())
        self.assertEqual("Saldo de 110.0 do titular Marcos", marcos_account.statement())


if __name__ == '__main__':
    unittest.main()
