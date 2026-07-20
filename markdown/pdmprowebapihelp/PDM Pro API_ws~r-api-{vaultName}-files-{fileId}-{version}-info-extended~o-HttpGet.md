---
title: "api/{vaultName}/files/{fileId}/{version}/info/extended (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-info-extended"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-info-extended~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/info/extended (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/info/extended |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/info/extended (Get) |
| --- |

Description

Get file info extended

Gets extended file information.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| version | (URI parameter) Version (required) | integer |
| StateId | (Response) State ID Member of VersionInfoExtended model | integer |
| State | (Response) State name Member of VersionInfoExtended model | string |
| Workflow | (Response) Workflow name Member of VersionInfoExtended model | string |
| Category | (Response) Category Member of VersionInfoExtended model | string |
| ReplicatedTo | (Response) Replicated to Member of VersionInfoExtended model | string |
| Branches | (Response) Branches Member of VersionInfoExtended model | string |

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

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
