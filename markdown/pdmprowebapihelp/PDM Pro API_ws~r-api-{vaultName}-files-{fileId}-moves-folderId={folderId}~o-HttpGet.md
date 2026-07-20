---
title: "api/{vaultName}/files/{fileId}/moves?folderId={folderId} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-moves-folderId={folderId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-moves-folderId={folderId}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/moves?folderId={folderId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/moves?folderId={folderId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/moves?folderId={folderId} (Get) |
| --- |

Description

Gets the history of moves for the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| folderId | (URI Parameter) Folder ID, default is 0 | integer |
| Source | (Response) Source Folder: FolderId: integer FolderPath: string (Member of HistoryMove) | Folder |
| Destination | (Response) Destination Folder: FolderId: integer FolderPath: string (Member of HistoryMove) | Folder |
| Date | (Response) Date (Member of HistoryMove) | date |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Source": {
      "FolderId": 1,
      "FolderPath": "sample string 2"
    },
    "Destination": {
      "FolderId": 1,
      "FolderPath": "sample string 2"
    },
    "Date": "2024-11-27T09:52:30.6956057-05:00"
  },
  {
    "Source": {
      "FolderId": 1,
      "FolderPath": "sample string 2"
    },
    "Destination": {
      "FolderId": 1,
      "FolderPath": "sample string 2"
    },
    "Date": "2024-11-27T09:52:30.6956057-05:00"
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfHistoryMove xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <HistoryMove>
    <Date>2024-11-27T09:52:30.6956057-05:00</Date>
    <Destination>
      <FolderId>1</FolderId>
      <FolderPath>sample string 2</FolderPath>
    </Destination>
    <Source>
      <FolderId>1</FolderId>
      <FolderPath>sample string 2</FolderPath>
    </Source>
  </HistoryMove>
  <HistoryMove>
    <Date>2024-11-27T09:52:30.6956057-05:00</Date>
    <Destination>
      <FolderId>1</FolderId>
      <FolderPath>sample string 2</FolderPath>
    </Destination>
    <Source>
      <FolderId>1</FolderId>
      <FolderPath>sample string 2</FolderPath>
    </Source>
  </HistoryMove>
</ArrayOfHistoryMove>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
