---
title: "api/{vaultName}/files/{fileId}/{version}/{folderId}/configurations (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-{folderId}-configurations"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-{folderId}-configurations~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/{folderId}/configurations (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/configurations |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/{folderId}/configurations (Get) |
| --- |

Description

Gets the configurations for the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| version | (Required URI Parameter) File version | integer |
| folderId | (URI Parameter) Folder ID, default is 0 | integer |
| ConfigurationName | (Response) Configuration name (Member of Config Model) | string |
| ConfigurationId | (Response) Configuration ID (Member of Config Model) | integer |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "ConfigurationName": "sample string 1",
    "ConfigurationId": 2
  },
  {
    "ConfigurationName": "sample string 1",
    "ConfigurationId": 2
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfConfig xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Config>
    <ConfigurationId>2</ConfigurationId>
    <ConfigurationName>sample string 1</ConfigurationName>
  </Config>
  <Config>
    <ConfigurationId>2</ConfigurationId>
    <ConfigurationName>sample string 1</ConfigurationName>
  </Config>
</ArrayOfConfig>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
