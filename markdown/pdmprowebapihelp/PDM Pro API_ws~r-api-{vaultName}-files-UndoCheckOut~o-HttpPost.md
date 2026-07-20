---
title: "api/{vaultName}/files/UndoCheckOut (Post)"
project: ""
interface: "r-api-{vaultName}-files-UndoCheckOut"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-UndoCheckOut~o-HttpPost.html"
---

# api/{vaultName}/files/UndoCheckOut (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/files/UndoCheckOut |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/UndoCheckOut (Post) |
| --- |

Description

POST: api/{VaultName}/files/UndoCheckOut Undo lock file

Unlocks the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| FileId | (Body and response parameter) File ID Member of CheckOutItem and UnLockResultModel models | integer |
| FolderId | (Body parameter) Folder ID Member of CheckOutItem model | integer |
| IsSuccess | (Response) Whether unlock is successful Member of UndoLockResultModel model | boolean |
| Warning | (Response) A BaseWarningModel object that consists of: Message (string) IsBlocking (boolean) IsError (boolean) Member of UndoLockResultModel model | BaseWarningModel |

Request (application/json, text/json)

#### Sample Data

```
[
  {
    "FileId": 1,
    "FolderId": 2
  },
  {
    "FileId": 1,
    "FolderId": 2
  }
]
```

Request (application/xml, text/xml)

#### Sample Data

```
<ArrayOfCheckOutItem xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <CheckOutItem>
    <FileId>1</FileId>
    <FolderId>2</FolderId>
  </CheckOutItem>
  <CheckOutItem>
    <FileId>1</FileId>
    <FolderId>2</FolderId>
  </CheckOutItem>
</ArrayOfCheckOutItem>
```

Request (application/x-www-form-urlencoded)

Response (application/json, text/json, application/xml, text/xml)

Example

[Check Out Files in PDM Vault.postman_collection.json](Check%20Out%20Files%20in%20PDM%20Vault.postman_collection.json)

Remarks

This operation:

- takes an array of CheckOutItems.
- returns an array of UndoLockResultModels.

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
