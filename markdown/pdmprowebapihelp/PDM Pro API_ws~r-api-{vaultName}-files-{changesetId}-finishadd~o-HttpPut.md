---
title: "api/{vaultName}/files/{changesetId}/finishadd (Put)"
project: ""
interface: "r-api-{vaultName}-files-{changesetId}-finishadd"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{changesetId}-finishadd~o-HttpPut.html"
---

# api/{vaultName}/files/{changesetId}/finishadd (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/files/{changesetId}/finishadd |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Stage Resource Group : api/{vaultName}/files/{changesetId}/finishadd (Put) |
| --- |

Description

PUT: api/{vaultName}/files/{changesetId}/finishadd Finish of add file operation. This method adds files from changeset to the vault.

Adds files in the specified changeset to the vault. (See**Remarks**)

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| changesetId | (URI parameter) Changeset ID (required) | integer |
| Content | (Response) GUID of the add operation; use the GUID to query the progress/status of the add operation (see api/{vaultName}/progress/{guid}/status ) Member of HttpResponseMessage model | HttpContent |

Example

[Upload SOLIDWORKS Files to PDM Vault.postman_collection.json](Upload%20SOLIDWORKS%20Files%20to%20PDM%20Vault.postman_collection.json)

Remarks

Before sending this HTTP request you must send[api/{vaultName}/files/{changesetId}/upload (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{changesetId}-upload~o-HttpPut.html)to get a changeset ID.

This request returns a GUID that you can use in further calls to check progress:[api/{vaultName}/progress/{guid}/status (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-progress-{guid}-status~o-HttpGet.html)and[api/{vaultName}/progress/{guid}/result (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-progress-{guid}-result~o-HttpGet.html)

See Also

[Stage Resource Group](PDM%20Pro%20API_ws~g-ab7aa0c7-6261-4685-9682-f6301732b3ab.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
