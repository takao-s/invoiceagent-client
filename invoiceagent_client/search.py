from invoiceagent_client.common import CommonMixin


class Search(CommonMixin):
    def search_documents(self, data, version="v19"):
        path = f"/search_{version}/folder"
        return self.post_json(path=path, data=data)

    def search_in_document(self, file_id: str, data, version="v2"):
        path = f"/search_{version}/documents/{file_id}"
        headers = {'Accept': 'application/json'}
        return self.post(path=path, headers=headers, data=data)

    def search_cancel(self):
        path = "/search/cancel"
        return self.get(path=path)
