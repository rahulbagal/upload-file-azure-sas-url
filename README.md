# Azure Storage - Upload File - Python

**Upload File to Azure Blob Storage using SAS token / SAS url**

Azure Blob Storage can be access using SAS ( shared access signatures) token. 

This code is used in scenarios such as, SAS URL / SAS token is issued by one application to another application.
Receiving application uploads a file to blob storage using that SAS token.

- Pass SAS url & file name with path to function `upload_using_sas(sas_url , file_name_full_path)`
- Its parses SAS url and sends file using HTTP PUT request. 
- It also recognizes content type from file extension.
- Returns upload status as HTTP status code ( 201 - Accepted is success )

Install following packages referenced in the code 

```
pip install requests 
pip install azure-storage-blob
```

Refer code from `main.py` to know how to use this function.
