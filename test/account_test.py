import unittest

from src.account import Account


class AccountTestCase(unittest.TestCase):

    def test_account(self):
        account = Account(123, "Eu Ddono", 55.5, 1000.0)
        self.assertEqual(123, account.number)


if __name__ == '__main__':
    unittest.main()
