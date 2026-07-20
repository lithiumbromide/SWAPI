---
title: "api/{vaultName}/configuration/hooks/url (Post)"
project: ""
interface: "r-api-{vaultName}-configuration-hooks-url"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-configuration-hooks-url~o-HttpPost.html"
---

# api/{vaultName}/configuration/hooks/url (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/configuration/hooks/url |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Configuration Resource Group : api/{vaultName}/configuration/hooks/url (Post) |
| --- |

Description

Sets the webhooks for the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | Name of vault to get and set webhooks | string |

Request (application/json, text/json)

#### Sample Data

```
{
  "sample string 1": [
    "sample string 1",
    "sample string 2"
  ],
  "sample string 2": [
    "sample string 1",
    "sample string 2"
  ]
}
```

Request (application/xml, text/xml)

#### Sample Data

```
<ArrayOfKeyValueOfstringArrayOfstringty7Ep6D1 xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
  <KeyValueOfstringArrayOfstringty7Ep6D1>
    <Key>sample string 1</Key>
    <Value>
      <string>sample string 1</string>
      <string>sample string 2</string>
    </Value>
  </KeyValueOfstringArrayOfstringty7Ep6D1>
  <KeyValueOfstringArrayOfstringty7Ep6D1>
    <Key>sample string 2</Key>
    <Value>
      <string>sample string 1</string>
      <string>sample string 2</string>
    </Value>
  </KeyValueOfstringArrayOfstringty7Ep6D1>
</ArrayOfKeyValueOfstringArrayOfstringty7Ep6D1>
```

Request (application/x-www-form-urlencoded)

Response (application/json, text/json, application/xml, text/xml)

Example

Click and save the following to your computer. Then drag/drop it into Postman:

[HooksManagement.postman_collection.json](HooksManagement.postman_collection.json)

Remarks

To use this API, you must authenticate this request with a token and select the CanAdministrateAddins permission in the Admin tool.

See the[PDM Pro Web API Webhooks Programming Guide](PDMProWebAPI_Webhooks_Programming_Guide.html).

See Also

[Configuration Resource Group](PDM%20Pro%20API_ws~g-985b99d2-3678-4b90-b592-fc1b4707401e.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
