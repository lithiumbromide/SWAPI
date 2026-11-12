---
title: "api/{vaultName}/notifications/markRead (Post)"
project: ""
interface: "r-api-{vaultName}-notifications-markRead"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-notifications-markRead~o-HttpPost.html"
---

# api/{vaultName}/notifications/markRead (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/notifications/markRead |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Notification Resource Group : api/{vaultName}/notifications/markRead (Post) |
| --- |

Description

POST: api/{vaultName}/notifications/markRead Mark message as read

Marks a notification as read.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| IsValid | (Response) Whether the mark is valid Member of ValidationOptionOfint32 | boolean |
| Warning | (Response) A BaseWarningModel object that consists of: Message (string) IsBlocking (boolean) IsError (boolean) Member of ValidationOptionOfint32 | BaseWarningModel |
| Value | (Response) Value of response Member of ValidationOptionOfint32 | integer |

Request (application/json, text/json)

#### Sample Data

```
[
  1,
  2
]
```

Request (application/xml, text/xml)

#### Sample Data

```
<ArrayOfint xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
  <int>1</int>
  <int>2</int>
</ArrayOfint>
```

Request (application/x-www-form-urlencoded)

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "IsValid": false,
    "Warning": null,
    "Value": 0
  },
  {
    "IsValid": false,
    "Warning": null,
    "Value": 0
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfValidationOptionOfint xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ValidationOptionOfint />
  <ValidationOptionOfint />
</ArrayOfValidationOptionOfint>
```

Remarks

This operation:

- takes a body parameter array of integers that are notification IDs.
- returns an array of ValidationOptionOfint objects.

See Also

[Notification Resource Group](PDM%20Pro%20API_ws~g-a913ab1d-ff6c-435e-bc6e-8e6294326caa.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
