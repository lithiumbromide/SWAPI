---
title: "api/{vaultName}/progress/{guid}/status (Get)"
project: ""
interface: "r-api-{vaultName}-progress-{guid}-status"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-progress-{guid}-status~o-HttpGet.html"
---

# api/{vaultName}/progress/{guid}/status (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/progress/{guid}/status |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Progress Resource Group : api/{vaultName}/progress/{guid}/status (Get) |
| --- |

Description

GET: api/{vaultName}/progress/{guid}/status Get operation status

Gets the status of the specified operation.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| guid | (URI parameter) Operation GUID (required) (See Remarks ) | string |
| Version | (Response) A Version model that consists of: Major (integer) Minor (integer) Build (integer) Revision (integer) MajorRevision (integer) MinorRevision (integer) Member of HttpResponseMessage model | Version |
| Content | (Response) Entity body and content headers Member of HttpResponseMessage model | HttpContent |
| StatusCode | (Response) Status code; see https://en.wikipedia.org/wiki/List_of_HTTP_status_codes Member of HttpResponseMessage model | HttpStatusCode |
| ReasonPhrase | (Response) Reason Member of HttpResponseMessage model | string |
| Headers | (Response) Array of headers Member of HttpResponseMessage model | Collection of Object |
| RequestMessage | (Response) An HttpRequestMessage object that consists of: Version (Version model) Content (HttpContent object consisting of Headers array) Method (HttpMethod object consisting of Method string) RequestUri (URI) Headers (array of objects) Properties (Dictionary of string [key] and Object [value] Member of HttpResponseMessage model | HttpRequestMessage |
| IsSuccessStatusCode | (Response) True if successful, false if not Member of HttpResponseMessage model | boolean |

Example

[Upload SOLIDWORKS Files to PDM Vault.postman_collection.json](Upload%20SOLIDWORKS%20Files%20to%20PDM%20Vault.postman_collection.json)

|

[Check in SOLIDWORKS Files in PDM Vault.postman_collection.json](Check%20in%20SOLIDWORKS%20Files%20%20in%20PDM%20Vault.postman_collection.json)

Remarks

The operation GUID can be found in the response of

[api/{vaultName}/files/{changesetId}/finishadd (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{changesetId}-finishadd~o-HttpPut.html)

.

See Also

[Progress Resource Group](PDM%20Pro%20API_ws~g-41efefa2-70af-440a-a06e-5d7156c5dc19.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
