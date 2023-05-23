import os
import unittest
from dotenv import load_dotenv
from invoiceagent_client import Client

load_dotenv()

USER = os.getenv('USERNAME')
PASS = os.getenv('PASS')
INSTANCE = os.getenv('INSTANCE')
FILE_ID = os.getenv('FILE_ID')

os.makedirs('downloads', exist_ok=True)


class ClientTest(unittest.TestCase):
    def test_dl_raw(self):
        iv = Client(user=USER, password=PASS, instance=INSTANCE)
        data = {
            'related': "false"
        }
        r = iv.download_raw_document(file_id=FILE_ID, data=data)

        with open('downloads/test_dl_raw.pdf', mode='wb') as fs:
            fs.write(r.content)

    def test_dl(self):
        iv = Client(user=USER, password=PASS, instance=INSTANCE)
        data = {
            'pages': "2-5"
        }
        r = iv.download_document(file_id=FILE_ID, data=data)

        with open('downloads/test_dl.pdf', mode='wb') as fs:
            fs.write(r.content)
