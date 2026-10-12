---
title: "api/{vaultName}/notifications (Post)"
project: ""
interface: "r-api-{vaultName}-notifications"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-notifications~o-HttpPost.html"
---

# api/{vaultName}/notifications (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/notifications |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Notification Resource Group : api/{vaultName}/notifications (Post) |
| --- |

Description

POST: api/{VaultName}/notifications Send message

Sends the specified message.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| RecipientId | (Body parameter) Recipient user ID Member of MsgInfo model | integer |
| Subject | (Body parameter) Subject text Member of MsgInfo model | string |
| Message | (Body parameter) Message text Member of MsgInfo model | string |
| Password | (Body parameter) Password Member of MsgInfo model | string |

Request (application/json, text/json)

#### Sample Data

```
{
  "RecipientId": 1,
  "Subject": "sample string 2",
  "Message": "sample string 3",
  "Password": "sample string 4"
}
```

Request (application/xml, text/xml)

#### Sample Data

```
<MsgInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Message>sample string 3</Message>
  <Password>sample string 4</Password>
  <RecipientId>1</RecipientId>
  <Subject>sample string 2</Subject>
</MsgInfo>
```

Request (application/x-www-form-urlencoded)

Response (application/json, text/json)

Returns the status of the operation; true if successful, false if not

#### Sample Data

```
true
```

Response (application/xml, text/xml)

Returns the status of the operation; true if successful, false if not

#### Sample Data

```
<boolean xmlns="http://schemas.microsoft.com/2003/10/Serialization/">true</boolean>
```

Remarks

This operation:

- takes MsgInfo body parameters.
- returns a boolean status.

See Also

[Notification Resource Group](PDM%20Pro%20API_ws~g-a913ab1d-ff6c-435e-bc6e-8e6294326caa.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
