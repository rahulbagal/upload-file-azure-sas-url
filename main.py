#!/usr/bin/env python

from azure_sas_upload import upload_using_sas
# SAS URL
sas_url_for_upload = ( "https://example.blob.core.windows.net/example?"
                        "st=2018-03-13T09%3A05%3A00Z&se=2019-03-14T09%3A05%3A00Z&sp=rw&sv=2015-12-11&sr=c&sig=IP45%2FplSvHbSJsW1UcEA7Y1tertiMIiiYq3uCbCjn%2FA%3D"
                      )
# File to upload
file_to_upload = "/path/to/file/filename.zip"

# Start upload
r= upload_using_sas(sas_url_for_upload, file_to_upload)
# Print upload status . 201 is success.
print ("Upload Status :" + str(r))
