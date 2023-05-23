from invoiceagent_client.common import CommonMixin


class Download(CommonMixin):
    def download_document(self, file_id: str, data, version="v4"):
        path = f"/download_{version}/{file_id}"
        headers = {'Accept': 'application/pdf'}
        # return self._download(method="POST", path=path, headers=headers, data=data)
        return self.post(path=path, headers=headers, data=data)

    def download_raw_document(self, file_id: str, data=None, version="v3"):
        path = f"/download_{version}/raw/{file_id}"
        return self.get(path=path, data=data)

    def download_print_document(self, file_id: str, data=None, version="v2"):
        path = f"/download_{version}/print/{file_id}"
        headers = {'Accept': 'application/pdf'}
        # return self._download(method="POST", path=path, headers=headers, data=data)
        return self.post(path=path, headers=headers, data=data)

    def download_packed_documents(self, data, version="v5"):
        path = f"/download_{version}/packed"
        headers = {'Accept': 'application/zip'}
        return self.post(path=path, headers=headers, data=data)

    def download_packed_documents_file_get(self, receptionId: str):
        path = f"/download/packed/{receptionId}"
        # return self._download(method="GET", path=path)
        return self.get(path=path)

    def download_packed_documents_status(self):
        path = "/download/packed/status"
        return self.get(path=path)
