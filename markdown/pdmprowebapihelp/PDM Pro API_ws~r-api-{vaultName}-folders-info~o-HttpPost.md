---
title: "api/{vaultName}/folders/info (Post)"
project: ""
interface: "r-api-{vaultName}-folders-info"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-folders-info~o-HttpPost.html"
---

# api/{vaultName}/folders/info (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/folders/info |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Folder Resource Group : api/{vaultName}/folders/info (Post) |
| --- |

Description

POST: api/{VaultName}/folders/info Get folder info

Gets information about specified folders in the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Name of vault | string |
| WarningMessage | (Response) Warning message Member of FolderInfoExtended model | string |
| Folder | (Response) Folder model that consists of: Folder ID Folder path Member of FolderInfoExtended model | Folder |
| FolderName | (Response) Folder name Member of FolderInfoExtended model | string |
| ParentFolderId | (Response) ID of parent folder Member of FolderInfoExtended model | integer |

Request (application/json, text/json)

Array of folder IDs as body parameter

#### Sample Data

```
[
  1,
  2
]
```

Request (application/xml, text/xml)

Array of folder IDs as body parameter

#### Sample Data

```
<ArrayOfint xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
  <int>1</int>
  <int>2</int>
</ArrayOfint>
```

Request (application/x-www-form-urlencoded)

Array of folder IDs as body parameter

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "WarningMessage": "sample string 1",
    "Folder": {
      "FolderId": 1,
      "FolderPath": "sample string 2"
    },
    "FolderName": "sample string 2",
    "ParentFolderId": 3
  },
  {
    "WarningMessage": "sample string 1",
    "Folder": {
      "FolderId": 1,
      "FolderPath": "sample string 2"
    },
    "FolderName": "sample string 2",
    "ParentFolderId": 3
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfFolderInfoExtended xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <FolderInfoExtended>
    <Folder>
      <FolderId>1</FolderId>
      <FolderPath>sample string 2</FolderPath>
    </Folder>
    <FolderName>sample string 2</FolderName>
    <ParentFolderId>3</ParentFolderId>
    <WarningMessage>sample string 1</WarningMessage>
  </FolderInfoExtended>
  <FolderInfoExtended>
    <Folder>
      <FolderId>1</FolderId>
      <FolderPath>sample string 2</FolderPath>
    </Folder>
    <FolderName>sample string 2</FolderName>
    <ParentFolderId>3</ParentFolderId>
    <WarningMessage>sample string 1</WarningMessage>
  </FolderInfoExtended>
</ArrayOfFolderInfoExtended>
```

See Also

[Folder Resource Group](PDM%20Pro%20API_ws~g-ebc7dbbc-e61a-4479-954a-e443044cd655.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
