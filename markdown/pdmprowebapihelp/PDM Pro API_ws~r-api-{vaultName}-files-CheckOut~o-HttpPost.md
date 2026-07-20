---
title: "api/{vaultName}/files/CheckOut (Post)"
project: ""
interface: "r-api-{vaultName}-files-CheckOut"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-CheckOut~o-HttpPost.html"
---

# api/{vaultName}/files/CheckOut (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/files/CheckOut |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/CheckOut (Post) |
| --- |

Description

POST: api/{VaultName}/files/CheckOut Lock file

Checks out the specified file(s).

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| FileId | (Body and response parameter) File ID Member of CheckOutResultModel model | integer |
| FolderId | (Body parameter) Folder ID | integer |
| IsSuccess | (Response) Whether the check out is successful Member of CheckOutResultModel model | boolean |
| Warning | (Response) A BaseWarningModel object that consists of: Message (string) IsBlocking (boolean) IsError (boolean) Member of CheckOutResultModel model | Collection of BaseWarningModel |

Request (application/json, text/json)

The body parameter consists of arrays of FileId and FolderId.

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

The body parameter consists of arrays of FileId and FolderId.

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

The body parameter consists of arrays of FileId and FolderId.

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "FileId": 1,
    "IsSuccess": true,
    "Warning": null
  },
  {
    "FileId": 1,
    "IsSuccess": true,
    "Warning": null
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfCheckOutResultModel xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <CheckOutResultModel>
    <FileId>1</FileId>
    <IsSuccess>true</IsSuccess>
    <Warning i:nil="true" />
  </CheckOutResultModel>
  <CheckOutResultModel>
    <FileId>1</FileId>
    <IsSuccess>true</IsSuccess>
    <Warning i:nil="true" />
  </CheckOutResultModel>
</ArrayOfCheckOutResultModel>
```

Example

[Check Out Files in PDM Vault.postman_collection.json](Check%20Out%20Files%20in%20PDM%20Vault.postman_collection.json)

|

[Modify File Datacards.postman_collection.json](Modify%20File%20Datacards.postman_collection.json)

Remarks

This operation returns the file ID, IsSuccess, and Warning.

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
