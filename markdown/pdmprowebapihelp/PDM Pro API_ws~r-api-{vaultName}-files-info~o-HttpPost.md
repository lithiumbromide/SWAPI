---
title: "api/{vaultName}/files/info (Post)"
project: ""
interface: "r-api-{vaultName}-files-info"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-info~o-HttpPost.html"
---

# api/{vaultName}/files/info (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/files/info |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/info (Post) |
| --- |

Description

POST: api/{VaultName}/files/info

Gets information about the specified files.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| Id | (Response) File ID Member of ObjectInfo model; see Remarks | integer |
| Name | (Response) File name Member of ObjectInfo model; see Remarks | string |
| Size | (Response) File size Member of ObjectInfo model; see Remarks | integer |
| ModifiedDate | (Response) Modification date Member of ObjectInfo model; see Remarks | date |
| Version | (Response) Version | integer |
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

Request (application/json, text/json)

Array of file IDs as body parameter

#### Sample Data

```
[
  1,
  2
]
```

Request (application/xml, text/xml)

Array of file IDs as body parameter

#### Sample Data

```
<ArrayOfint xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
  <int>1</int>
  <int>2</int>
</ArrayOfint>
```

Request (application/x-www-form-urlencoded)

Array of file IDs as body parameter

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Id": 1,
    "Name": "sample string 2",
    "Size": 3,
    "ModifiedDate": "2024-11-27T09:52:30.6715765-05:00",
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
    "ModifiedDate": "2024-11-27T09:52:30.6715765-05:00",
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
    <ModifiedDate>2024-11-27T09:52:30.6715765-05:00</ModifiedDate>
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
    <ModifiedDate>2024-11-27T09:52:30.6715765-05:00</ModifiedDate>
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

This operation:

- takes an array of body parameters that are IDs of files for which to get information.
- returns an array of ObjectInfos, one for each file ID.

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
