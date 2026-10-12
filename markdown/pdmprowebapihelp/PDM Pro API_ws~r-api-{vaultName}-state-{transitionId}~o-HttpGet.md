---
title: "api/{vaultName}/state/{transitionId} (Get)"
project: ""
interface: "r-api-{vaultName}-state-{transitionId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-{transitionId}~o-HttpGet.html"
---

# api/{vaultName}/state/{transitionId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/state/{transitionId} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > State Transition Resource Group : api/{vaultName}/state/{transitionId} (Get) |
| --- |

Description

GET: api/{vaultName}/state/{transitionId} Get transition info

Gets information about the specified transition.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| transitionId | (URI and response parameter) Transition ID (URI required) Member of TransitionInfo model | integer |
| TransitionName | (Response) Transition name Member of TransitionInfo model | string |
| Type | (Response) A TransitionType; one of: Normal = 0 Automatic = 1 Parallel = 2 Member of TransitionInfo model | TransitionType |
| Authentication | (Response) Whether authentication is required Member of TransitionInfo model | boolean |

Response (application/json, text/json)

#### Sample Data

```
{
  "TransitionName": "sample string 1",
  "TransitionId": 2,
  "Type": 0,
  "Authentication": true
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<TransitionInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Authentication>true</Authentication>
  <TransitionId>2</TransitionId>
  <TransitionName>sample string 1</TransitionName>
  <Type>Normal</Type>
</TransitionInfo>
```

See Also

[State Transition Resource Group](PDM%20Pro%20API_ws~g-7b85dfc9-ca5f-4c42-8689-253a31d91dce.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
