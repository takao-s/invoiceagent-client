from invoiceagent_client.archives import Archives
from invoiceagent_client.doc_ope import DocOpe
from invoiceagent_client.download import Download
from invoiceagent_client.preview import Preview
from invoiceagent_client.search import Search


class Client(Archives,
             DocOpe,
             Download,
             Preview,
             Search):
    def __init__(
            self,
            user,
            password,
            instance,
            iv_domain: str = "local"):

        self.endpoint = f"https://{instance}.spa-cloud.com/spa/service"
        self.xsrf_token = None
        self.cookies = None

        data = {
            'user': user,
            'password': password,
            'domain': iv_domain
        }

        self.post(path="/auth/login", data=data)
