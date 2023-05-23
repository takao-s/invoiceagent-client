import os
import unittest
from urllib import parse
from dotenv import load_dotenv
from invoiceagent_client import Client

load_dotenv()

USER = os.getenv('USERNAME')
PASS = os.getenv('PASS')
INSTANCE = os.getenv('INSTANCE')
FOLDER_ID = os.getenv('FOLDER_ID')


class ClientTest(unittest.TestCase):
    def test_archive(self):
        iv = Client(user=USER, password=PASS, instance=INSTANCE)

        name = "sample file.pdf"
        data = {
            'folderId': FOLDER_ID,
            'name': parse.unquote(name),
            'docTypeId': 133,
            'overwrite': True,
            'overwriteLinkSource': False,
            'overwriteUpdate': True,
            'force': False,
        }

        custom_props = {
            "customProperties": {
                "100": "text",
                "101": "text",
            }
        }
        f_path = os.path.join(os.getcwd(), 'downloads', 'test_dl.pdf')
        print(f_path)
        file = open(f_path, mode='+rb')

        iv.archives(data=data, file=file, custom_props=custom_props)
        print(iv.xsrf_token)
        self.assertIsNotNone(iv.xsrf_token)
