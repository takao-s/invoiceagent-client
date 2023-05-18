from invoiceagent_client.common import CommonMixin


class Preview(CommonMixin):
    def preview_get(self, file_id: str, page: str, data, version="v5"):
        path = f"/preview_{version}/{file_id}/{page}"
        return self._download(method="GET", path=path, data=data)

    def highlight_get(self, file_id: str, page: str, data, version="v9"):
        path = f"/highlight_{version}/{file_id}/{page}"
        r = self.post_json(path=path, data=data)
        return r.json()
