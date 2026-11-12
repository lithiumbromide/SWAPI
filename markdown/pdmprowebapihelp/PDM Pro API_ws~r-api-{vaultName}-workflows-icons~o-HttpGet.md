---
title: "api/{vaultName}/workflows/icons (Get)"
project: ""
interface: "r-api-{vaultName}-workflows-icons"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-workflows-icons~o-HttpGet.html"
---

# api/{vaultName}/workflows/icons (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/workflows/icons |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Workflow Resource Group : api/{vaultName}/workflows/icons (Get) |
| --- |

Description

GET: api/{vaultName}/workflows/icons Get state icons

Gets the workflow state icons in the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| Item1 | (Response) ID of icon Member of TupleOfint32AndString model | integer |
| Item2 | (Response) Name of icon Member of TupleOfint32AndString model | string |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "m_Item1": 1,
    "m_Item2": "sample string 2"
  },
  {
    "m_Item1": 1,
    "m_Item2": "sample string 2"
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfTupleOfintstring xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/System">
  <TupleOfintstring>
    <m_Item1>1</m_Item1>
    <m_Item2>sample string 2</m_Item2>
  </TupleOfintstring>
  <TupleOfintstring>
    <m_Item1>1</m_Item1>
    <m_Item2>sample string 2</m_Item2>
  </TupleOfintstring>
</ArrayOfTupleOfintstring>
```

See Also

[Workflow Resource Group](PDM%20Pro%20API_ws~g-9f5fba41-ad72-44e1-a9f2-866fdf258ef8.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
