---
title: "api/{vaultName}/users/{userId}/Extended (Put)"
project: ""
interface: "r-api-{vaultName}-users-{userId}-Extended"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-users-{userId}-Extended~o-HttpPut.html"
---

# api/{vaultName}/users/{userId}/Extended (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/users/{userId}/Extended |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > User Resource Group : api/{vaultName}/users/{userId}/Extended (Put) |
| --- |

Description

PUT: api/{VaultName}/users/{UserID}/Extended Set user info extended

Saves information about the specified user.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| userId | (URI parameter) User ID (required) | integer |
| UserInfo | (Response) A UserInfo object that consists of: UserName (string) UserId (integer) Member of UserInfoExtended model (Body parameter) A UserInfo object that consists of: UserName (string) UserId (integer) Member of UserInfoExtended model | UserInfo |
| Email | (Response) User email Member of UserInfoExtended model (Body parameter) | string |
| FullName | (Response) User full name Member of UserInfoExtended model (Body parameter) Member of UserInfoExtended model | string |
| Initials | (Response) User intials Member of UserInfoExtended model (Body parameter) Member of UserInfoExtended model | string |
| Phone | (Response) User phone Member of UserInfoExtended model (Body parameter) Member of UserInfoExtended model | string |
| Cellphone | (Response) User mobile phone Member of UserInfoExtended model (Body parameter) Mobile phone Member of UserInfoExtended model | string |

Request (application/json, text/json)

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

Request (application/xml, text/xml)

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

Request (application/x-www-form-urlencoded)

Response (application/json, text/json)

#### Sample Data

```
true
```

Response (application/xml, text/xml)

#### Sample Data

```
<boolean xmlns="http://schemas.microsoft.com/2003/10/Serialization/">true</boolean>
```

See Also

[User Resource Group](PDM%20Pro%20API_ws~g-09a63486-9278-41ff-970c-d47012e2bea1.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
