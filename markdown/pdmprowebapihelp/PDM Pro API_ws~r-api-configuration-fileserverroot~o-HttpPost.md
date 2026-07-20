---
title: "api/configuration/fileserverroot (Post)"
project: ""
interface: "r-api-configuration-fileserverroot"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-configuration-fileserverroot~o-HttpPost.html"
---

# api/configuration/fileserverroot (Post)

PDM Pro API Web Service

| Post | api/configuration/fileserverroot |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Configuration Resource Group : api/configuration/fileserverroot (Post) |
| --- |

Description

POST: api/configuration/fileserverroot
Add file server root pathMigrates add-ins from previous file server root to the specified new one and reloads hooks instances.

Request (application/json, text/json)

#### Sample Data

```
"sample string 1"
```

Request (application/xml, text/xml)

#### Sample Data

```
<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">sample string 1</string>
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

Example

Click and save the following to your computer. Then drag/drop it into Postman:

[GetPostFileServerRoot.postman_collection.json](GetPostFileServerRoot.postman_collection.json)

In Postman, modify the Body of fileserverroot (Post) for your file server root location.

Remarks

See the

[PDM Pro Web API Webhooks Programming Guide](PDMProWebAPI_Webhooks_Programming_Guide.html)

.

See Also

[Configuration Resource Group](PDM%20Pro%20API_ws~g-985b99d2-3678-4b90-b592-fc1b4707401e.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
