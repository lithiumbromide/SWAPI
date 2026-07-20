---
title: "api/{vaultName}/files/{fileId}/{version}/{folderId} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-{folderId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-{folderId}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/{folderId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/{folderId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/{folderId} (Get) |
| --- |

Description

Gets information about the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| version | (URI Parameter) File version, default value is 0 | integer |
| folderId | (URI Parameter) Folder ID, default value is 0 | integer |
| Id | (Response) File ID (Member of ObjectInfo model) | integer |
| Name | (Response) File name (Member of ObjectInfo model) | string |
| Size | (Response) File size (Member of ObjectInfo model) | integer |
| ModifiedDate | (Response) Modified date (Member of ObjectInfo model) | date |
| State | (Response) File state (Member of ObjectInfo model) | string |
| StateId | (Response) File state ID (Member of ObjectInfo model) | integer |
| ParentFolderId | (Response) Parent folder ID (Member of ObjectInfo model) | integer |
| Path | (Response) Folder path (Member of ObjectInfo model) | string |
| Type | (Response) Object Type: Folder = 0 File = 1 Bom = 3 (Member of ObjectInfo model) | ObjectType |
| IsLocked | (Response) Whether file is locked (checked out) (Member of ObjectInfo model) | integer |
| LockedBy | (Response) ID of user who checked out the file (Member of ObjectInfo model) | integer |
| IsShared | (Response) Whether the file is shared (Member of ObjectInfo model) | integer |
| IsToolbox | (Response) 1 if a ToolBox item, 0 if not (Member of ObjectInfo model) | integer |
| IsDeleted | (Response) Whether file is deleted (Member of ObjectInfo model) | integer |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Id": 1,
    "Name": "sample string 2",
    "Size": 3,
    "ModifiedDate": "2024-11-27T09:52:30.6575844-05:00",
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
    "ModifiedDate": "2024-11-27T09:52:30.6575844-05:00",
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
    <ModifiedDate>2024-11-27T09:52:30.6575844-05:00</ModifiedDate>
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
    <ModifiedDate>2024-11-27T09:52:30.6575844-05:00</ModifiedDate>
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

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
