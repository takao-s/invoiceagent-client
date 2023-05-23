import os
import unittest
from dotenv import load_dotenv
from invoiceagent_client import Client

load_dotenv()

USER = os.getenv('USERNAME')
PASS = os.getenv('PASS')
INSTANCE = os.getenv('INSTANCE')
FILE_ID = os.getenv('FILE_ID')


class ClientTest(unittest.TestCase):
    def test_login(self):
        iv = Client(user=USER, password=PASS, instance=INSTANCE)
        print(iv.xsrf_token)
        self.assertIsNotNone(iv.xsrf_token)
