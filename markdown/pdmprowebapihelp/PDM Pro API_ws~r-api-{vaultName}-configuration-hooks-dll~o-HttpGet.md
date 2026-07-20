---
title: "api/{vaultName}/configuration/hooks/dll (Get)"
project: ""
interface: "r-api-{vaultName}-configuration-hooks-dll"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-configuration-hooks-dll~o-HttpGet.html"
---

# api/{vaultName}/configuration/hooks/dll (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/configuration/hooks/dll |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Configuration Resource Group : api/{vaultName}/configuration/hooks/dll (Get) |
| --- |

Description

Retrieves the list of add-in hooks from the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | Name of vault to get, put, and delete add-in hook DLLs | string |

Response (application/json, text/json, application/xml, text/xml)

Example

Click and save the following to your computer. Then drag/drop it into Postman:

[HooksManagement.postman_collection.json](HooksManagement.postman_collection.json)

Remarks

To use this API, you must create a**storage\addins\vault_name**folder in your file server root directory and add a Header called download to this request.

If download is set to:

- false, you must authenticate this request with a token. A list of relative path filenames is returned.
- true, you must authenticate this request with a token and select the CanAdministrateAddins permission in the Admin tool. A ZIP file containing all of the add-in hooks is downloaded.

See the[PDM Pro Web API Webhooks Programming Guide](PDMProWebAPI_Webhooks_Programming_Guide.html).

See Also

[Configuration Resource Group](PDM%20Pro%20API_ws~g-985b99d2-3678-4b90-b592-fc1b4707401e.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
