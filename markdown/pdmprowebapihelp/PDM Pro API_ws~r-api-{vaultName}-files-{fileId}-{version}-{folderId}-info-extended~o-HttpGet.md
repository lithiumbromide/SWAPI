---
title: "api/{vaultName}/files/{fileId}/{version}/{folderId}/info/extended (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-{folderId}-info-extended"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-{folderId}-info-extended~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/{folderId}/info/extended (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/info/extended |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/{folderId}/info/extended (Get) |
| --- |

Description

Gets extended version information for a specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| version | (Required URI Parameter) File version | integer |
| folderId | (URI Parameter) Folder ID, default is 0 | integer |
| StateId | (Response) State ID (Member of VersionInfoExtended Member) | integer |
| State | (Response) State name (Member of VersionInfoExtended Member) | string |
| Workflow | (Response) Workflow (Member of VersionInfoExtended Member) | string |
| Category | (Response) Category (Member of VersionInfoExtended Member) | string |
| ReplicatedTo | (Response) Replicated to (Member of VersionInfoExtended Member) | string |
| Branches | (Response) Branches (Member of VersionInfoExtended Member) | string |

Response (application/json, text/json)

#### Sample Data

```
{
  "StateId": 1,
  "State": "sample string 2",
  "Workflow": "sample string 3",
  "Category": "sample string 4",
  "ReplicatedTo": "sample string 5",
  "Branches": "sample string 6"
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<VersionInfoExtended xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Branches>sample string 6</Branches>
  <Category>sample string 4</Category>
  <ReplicatedTo>sample string 5</ReplicatedTo>
  <State>sample string 2</State>
  <StateId>1</StateId>
  <Workflow>sample string 3</Workflow>
</VersionInfoExtended>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
