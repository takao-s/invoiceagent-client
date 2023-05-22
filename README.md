# invoiceAgent Client

invoiceAgent Client is the python library for Web-API of invoiceAgent(WingArc1st Inc.).

# How to use

```python

from invoiceagent_client import Client

username = "Your_username"
password = "Your_password"
instance = "Your_instance"

# Initialize Client
iv = Client(user=username, passowrd=password, instance=instance)

# Archive file
name = "sample file.pdf"
data = {
    'folderId': "Target_folder_id",
    'name': "Your_filename",
}

file = open("/path/to/upload_file", mode='+rb')
iv.archives(data=data, file=file, custom_props=custom_props)

# Download file
data = {
    'pages': "1-2"
}
(filelikeo_bject, content_type, content_desposition) = iv.download_document(file_id="Source_folder_id", data=data)


```
