---
title: "api/{vaultName}/users/{userId}/Extended (Get)"
project: ""
interface: "r-api-{vaultName}-users-{userId}-Extended"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-users-{userId}-Extended~o-HttpGet.html"
---

# api/{vaultName}/users/{userId}/Extended (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/users/{userId}/Extended |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > User Resource Group : api/{vaultName}/users/{userId}/Extended (Get) |
| --- |

Description

GET: api/{VaultName}/users/{UserID}/Extended Get user info extended

Gets extended information about the specified user.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| userId | (URI parameter) User ID (required) | integer |
| UserInfo | (Body parameter) A UserInfo object that consists of: UserName (string) UserId (integer) Member of UserInfoExtended model (Response) A UserInfo object that consists of: UserName (string) UserId (integer) Member of UserInfoExtended model | UserInfo |
| Email | (Body parameter) (Response) User email Member of UserInfoExtended model | string |
| FullName | (Body parameter) Member of UserInfoExtended model (Response) User full name Member of UserInfoExtended model | string |
| Initials | (Body parameter) Member of UserInfoExtended model (Response) User intials Member of UserInfoExtended model | string |
| Phone | (Body parameter) Member of UserInfoExtended model (Response) User phone Member of UserInfoExtended model | string |
| Cellphone | (Body parameter) Mobile phone Member of UserInfoExtended model (Response) User mobile phone Member of UserInfoExtended model | string |

Response (application/json, text/json)

#### Sample Data

```
{
  "UserInfo": {
    "UserName": "sample string 1",
    "UserId": 2
  },
  "Email": "sample string 1",
  "FullName": "sample string 2",
  "Initials": "sample string 3",
  "Phone": "sample string 4",
  "Cellphone": "sample string 5"
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<UserInfoExtended xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Cellphone>sample string 5</Cellphone>
  <Email>sample string 1</Email>
  <FullName>sample string 2</FullName>
  <Initials>sample string 3</Initials>
  <Phone>sample string 4</Phone>
  <UserInfo>
    <UserId>2</UserId>
    <UserName>sample string 1</UserName>
  </UserInfo>
</UserInfoExtended>
```

See Also

[User Resource Group](PDM%20Pro%20API_ws~g-09a63486-9278-41ff-970c-d47012e2bea1.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
