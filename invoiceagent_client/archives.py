import json
from invoiceagent_client.common import CommonMixin


class Archives(CommonMixin):
    def archives(self, data, file, custom_props=None, content_type="application/pdf", version="v5"):
        path = f"/archives_{version}"
        headers = {'Accept': 'application/json'}
        files = {
            'file': ('', file, content_type)
        }

        if 'customProperties' in data.keys():
            if data['customProperties'] is tuple:
                raise Exception("customProperties attr must be str.")
        else:
            if custom_props:
                data['customProperties'] = json.dumps(custom_props)

        return self.post(path=path, headers=headers, data=data, files=files)
