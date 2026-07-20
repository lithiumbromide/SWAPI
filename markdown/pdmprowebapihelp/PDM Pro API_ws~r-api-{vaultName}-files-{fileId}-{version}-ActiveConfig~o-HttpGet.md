---
title: "api/{vaultName}/files/{fileId}/{version}/ActiveConfig (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-ActiveConfig"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-ActiveConfig~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/ActiveConfig (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/ActiveConfig |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/ActiveConfig (Get) |
| --- |

Description

Get active configuration

Gets the active configuration of the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| version | (URI parameter) Version (required) | integer |
| ConfigurationName | (Response) Active configuration name Member of Config model | string |
| ConfigurationId | (Response) Active configuration ID Member of Config model | integer |

Response (application/json, text/json)

#### Sample Data

```
{
  "ConfigurationName": "sample string 1",
  "ConfigurationId": 2
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<Config xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ConfigurationId>2</ConfigurationId>
  <ConfigurationName>sample string 1</ConfigurationName>
</Config>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
