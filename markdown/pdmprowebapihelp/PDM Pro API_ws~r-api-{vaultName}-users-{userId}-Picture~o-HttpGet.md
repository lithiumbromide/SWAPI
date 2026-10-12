---
title: "api/{vaultName}/users/{userId}/Picture (Get)"
project: ""
interface: "r-api-{vaultName}-users-{userId}-Picture"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-users-{userId}-Picture~o-HttpGet.html"
---

# api/{vaultName}/users/{userId}/Picture (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/users/{userId}/Picture |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > User Resource Group : api/{vaultName}/users/{userId}/Picture (Get) |
| --- |

Description

GET: api/{VaultName}/users/{UserID}/Picture Get user picture

Gets the picture of the specified user.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| userId | (URI parameter) User ID (required) | integer |
| Version | (Response) A Version model that consists of: Major (integer) Minor (integer) Build (integer) Revision (integer) MajorRevision (integer) MinorRevision (integer) Member of FileHttpResponseMessage model | Version |
| Content | (Response) Entity body and content headers Member of FileHttpResponseMessage model | HttpContent |
| StatusCode | (Response) Status code; see https://en.wikipedia.org/wiki/List_of_HTTP_status_codes Member of FileHttpResponseMessage model | HttpStatusCode |
| ReasonPhrase | (Response) Reason Member of FileHttpResponseMessage model | string |
| Headers | (Response) Collection of objects Member of FileHttpResponseMessage model | Collection of Object |
| RequestMessage | (Response) An HttpRequestMessage object that consists of: Version (Version model) Content (HttpContent object consisting of Headers array of objects) Method (HttpMethod object consisting of Method string) RequestUri (URI) Headers (Array of objects) Properties (Dictionary of string [key] and Object [value] Member of FileHttpResponseMessage model | HttpRequestMessage |
| IsSuccessStatusCode | (Response) True if successful, false if not Member of FileHttpResponseMessage model | boolean |

See Also

[User Resource Group](PDM%20Pro%20API_ws~g-09a63486-9278-41ff-970c-d47012e2bea1.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
