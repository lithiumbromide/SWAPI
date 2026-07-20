---
title: "api/{vaultName}/files/{fileId}/versions?folderId={folderId} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-versions-folderId={folderId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-versions-folderId={folderId}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/versions?folderId={folderId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/versions?folderId={folderId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/versions?folderId={folderId} (Get) |
| --- |

Description

GET: api/{VaultName}/files/{FileID}/versions Get file version info

Gets the specified file's version information.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI parameter) Vault name | string |
| fileId | (Required URI parameter) File ID | integer |
| folderId | (URI parameter) Folder ID (default value is 0) | integer |
| InfoType | (Response) Version information type: Version = 0 Revision = 1 Label = 2 Member of FileRevisionInfo model | Type |
| VersionNumber | (Response) Version; valid only if InfoType is 0 Member of FileRevisionInfo model | integer |
| Text | (Response) Label; valid only if InfoType is 2 Member of FileRevisionInfo model | string |
| Revision | (Response) Revision; valid only if InfoType is 1 Member of FileRevisionInfo model | string |
| FileSize | (Response) Size of file Member of FileRevisionInfo model | integer |
| VersionDate | (Response) Date of version, revision, or label Member of FileRevisionInfo model | date |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "InfoType": 0,
    "VersionNumber": 1,
    "Text": "sample string 2",
    "Revision": "sample string 3",
    "FileSize": 4,
    "VersionDate": "2024-11-27T09:52:30.3220305-05:00"
  },
  {
    "InfoType": 0,
    "VersionNumber": 1,
    "Text": "sample string 2",
    "Revision": "sample string 3",
    "FileSize": 4,
    "VersionDate": "2024-11-27T09:52:30.3220305-05:00"
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfFileRevisionInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <FileRevisionInfo>
    <FileSize>4</FileSize>
    <InfoType>Version</InfoType>
    <Revision>sample string 3</Revision>
    <Text>sample string 2</Text>
    <VersionDate>2024-11-27T09:52:30.3220305-05:00</VersionDate>
    <VersionNumber>1</VersionNumber>
  </FileRevisionInfo>
  <FileRevisionInfo>
    <FileSize>4</FileSize>
    <InfoType>Version</InfoType>
    <Revision>sample string 3</Revision>
    <Text>sample string 2</Text>
    <VersionDate>2024-11-27T09:52:30.3220305-05:00</VersionDate>
    <VersionNumber>1</VersionNumber>
  </FileRevisionInfo>
</ArrayOfFileRevisionInfo>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
