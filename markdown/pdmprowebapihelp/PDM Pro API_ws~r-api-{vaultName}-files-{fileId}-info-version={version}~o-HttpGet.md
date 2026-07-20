---
title: "api/{vaultName}/files/{fileId}/info?version={version} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-info-version={version}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-info-version={version}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/info?version={version} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/info?version={version} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/info?version={version} (Get) |
| --- |

Description

Get file info

Gets information about the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| version | (URI and Response parameter) Version (default value is 0) | integer |
| Id | (Response) File ID Member of ObjectInfo model; see Remarks | integer |
| Name | (Response) File name Member of ObjectInfo model; see Remarks | string |
| Size | (Response) File size Member of ObjectInfo model; see Remarks | integer |
| ModifiedDate | (Response) Modification date Member of ObjectInfo model; see Remarks | date |
| State | (Response) Workflow state Member of ObjectInfo model; see Remarks | string |
| StateId | (Response) State ID Member of ObjectInfo model; see Remarks | integer |
| ParentFolderId | (Response) Parent folder ID Member of ObjectInfo model; see Remarks | integer |
| Path | (Response) Folder path Member of ObjectInfo model; see Remarks | string |
| Type | (Response) ObjectType model; one of: Folder = 0 File = 1 Bom = 3 Member of ObjectInfo model; see Remarks | ObjectType |
| IsLocked | (Response) Whether the file is checked out Member of ObjectInfo model; see Remarks | integer |
| LockedBy | (Response) ID of user who checked out the file Member of ObjectInfo model; see Remarks | integer |
| IsShared | (Response) Whether the file is shared Member of ObjectInfo model; see Remarks | integer |
| IsToolbox | (Response) Whether the file is a toolbox item Member of ObjectInfo model; see Remarks | integer |
| IsDeleted | (Response) Whether the file is deleted Member of ObjectInfo model; see Remarks | integer |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Id": 1,
    "Name": "sample string 2",
    "Size": 3,
    "ModifiedDate": "2022-07-25T14:02:49.4594064-04:00",
    "Version": 5,
    "State": "sample string 6",
    "StateId": 7,
    "ParentFolderId": 8,
    "Path": "sample string 9",
    "Type": 0,
    "IsLocked": 10,
    "LockedBy": 11,
    "IsShared": 12,
    "IsToolbox": 13,
    "IsDeleted": 14
  },
  {
    "Id": 1,
    "Name": "sample string 2",
    "Size": 3,
    "ModifiedDate": "2022-07-25T14:02:49.4594064-04:00",
    "Version": 5,
    "State": "sample string 6",
    "StateId": 7,
    "ParentFolderId": 8,
    "Path": "sample string 9",
    "Type": 0,
    "IsLocked": 10,
    "LockedBy": 11,
    "IsShared": 12,
    "IsToolbox": 13,
    "IsDeleted": 14
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfObjectInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ObjectInfo>
    <Id>1</Id>
    <IsDeleted>14</IsDeleted>
    <IsLocked>10</IsLocked>
    <IsShared>12</IsShared>
    <IsToolbox>13</IsToolbox>
    <LockedBy>11</LockedBy>
    <ModifiedDate>2022-07-25T14:02:49.4594064-04:00</ModifiedDate>
    <Name>sample string 2</Name>
    <ParentFolderId>8</ParentFolderId>
    <Path>sample string 9</Path>
    <Size>3</Size>
    <State>sample string 6</State>
    <StateId>7</StateId>
    <Type>Folder</Type>
    <Version>5</Version>
  </ObjectInfo>
  <ObjectInfo>
    <Id>1</Id>
    <IsDeleted>14</IsDeleted>
    <IsLocked>10</IsLocked>
    <IsShared>12</IsShared>
    <IsToolbox>13</IsToolbox>
    <LockedBy>11</LockedBy>
    <ModifiedDate>2022-07-25T14:02:49.4594064-04:00</ModifiedDate>
    <Name>sample string 2</Name>
    <ParentFolderId>8</ParentFolderId>
    <Path>sample string 9</Path>
    <Size>3</Size>
    <State>sample string 6</State>
    <StateId>7</StateId>
    <Type>Folder</Type>
    <Version>5</Version>
  </ObjectInfo>
</ArrayOfObjectInfo>
```

Remarks

This operation should return one ObjectInfo object for each unique file ID in the request URI.

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
