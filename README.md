# Azure Storage - Upload File - Python

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

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


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-url]: https://github.com/IncubXperts/image_thumbnail_csharp/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/IncubXperts/image_thumbnail_csharp.svg?style=for-the-badge
[forks-url]: https://github.com/IncubXperts/image_thumbnail_csharp/network/members
[stars-shield]: https://img.shields.io/github/stars/IncubXperts/image_thumbnail_csharp.svg?style=for-the-badge
[stars-url]: https://github.com/IncubXperts/image_thumbnail_csharp/stargazers
[issues-shield]: https://img.shields.io/github/issues/IncubXperts/image_thumbnail_csharp.svg?style=for-the-badge
[issues-url]: https://github.com/IncubXperts/image_thumbnail_csharp/issues
[license-shield]: https://img.shields.io/github/license/IncubXperts/image_thumbnail_csharp.svg?style=for-the-badge
[license-url]: https://github.com/IncubXperts/image_thumbnail_csharp/blob/main/LICENSE
