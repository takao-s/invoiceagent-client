from invoiceagent_client.common import CommonMixin


class DocOpe(CommonMixin):
    def documents_lookup(self, data, version="v2"):
        path = f"/documents_{version}/lookup"
        r = self.post_json(path=path, data=data)
        return r.json()

    def documents_list(self, folder_id: str, data, version="v15"):
        path = f"/documents_{version}/{folder_id}/list"
        r = self.post(path=path, data=data)
        return r.json()

    def documents_get(self, file_id: str, data, version="v15"):
        path = f"/documents_{version}/{file_id}"
        r = self.post(path=path, data=data)
        return r.json()
