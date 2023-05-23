import logging
import requests
from requests import Response

logger = logging.getLogger(__name__)


class CommonMixin():
    def _request(self, method, path, headers={}, data=None, files=None, json=None, stream=False) -> Response:
        url = f"{self.endpoint}{path}"

        if self.xsrf_token:
            headers['X-XSRF-TOKEN'] = self.xsrf_token
            headers['X-Requested-With'] = 'XMLHttpRequest'

        if method == "POST":
            if files is not None:
                headers.pop('Content-Type')
            r = requests.post(url=url, cookies=self.cookies, headers=headers, data=data, json=json, files=files)

        elif method == "GET":
            r = requests.get(url=url, cookies=self.cookies, headers=headers, data=data, stream=stream)

        if r.status_code == 200:
            self.cookies = r.cookies if self.cookies is None else self.cookies
            if 'X-XSRF-TOKEN' in r.headers.keys():
                self.xsrf_token = r.headers['X-XSRF-TOKEN']
            return r
        else:
            logger.error(f"HTTP Status Code: {r.status_code}")
            for headerkey in [item for item in r.headers.keys() if item.startswith('X-Spa-Error')]:
                logger.error(f"{headerkey}: {r.headers[headerkey]}")
            raise

    def post(self, path, headers={}, data=None, stream=False, files=None) -> Response:
        return self._request(method="POST", path=path, headers=headers, data=data, stream=stream, files=files)

    def post_json(self, path, headers={}, data=None, stream=False, files=None) -> Response:
        return self._request(method="POST", path=path, headers=headers, json=data, stream=stream, files=files)

    def get(self, path, headers={}, data=None, stream=False) -> Response:
        return self._request(method="GET", path=path, headers=headers, data=data, stream=stream)
