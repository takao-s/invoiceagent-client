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
    def test_preview_get(self):
        iv = Client(user=USER, password=PASS, instance=INSTANCE)
        data = {
            'rotateType': "1"
        }
        r = iv.preview_get(file_id=FILE_ID, page=2, data=data)

        with open('downloads/test_dl_raw.png', mode='wb') as fs:
            fs.write(r.content)

    def test_hightlight_get(self):
        iv = Client(user=USER, password=PASS, instance=INSTANCE)
        data = {
            'highlightColor': "#0000FF",
            'searchWordInDocument': "あいうえお",
            'conditions': {
                "searchWord": "たちつてと",
            }
        }
        res = iv.highlight_get(file_id=635, page=2, data=data)

        print(res.json())
        self.assertIsNotNone(res.json())
