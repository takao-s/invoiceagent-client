import logging
from invoiceagent_client.client import Client

logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = [
    "Client"
]
