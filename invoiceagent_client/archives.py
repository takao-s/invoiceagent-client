import json
from invoiceagent_client.common import CommonMixin


class Archives(CommonMixin):
    def archives(self, data, file, custom_props=None, content_type="application/pdf", version="v5"):
        path = f"/archives_{version}"
        headers = {'Accept': 'application/json'}
        files = {
            'file': ('', file, content_type)
        }
        if 'customProperties' not in data.keys() and custom_props:
            data['customProperties'] = json.dumps(custom_props)

        r = self.post(path=path, headers=headers, data=data, files=files)
        return r.json()
