---
title: "api/{vaultName}/files/{fileId}/{version}/thumbnails (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-thumbnails"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-thumbnails~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/thumbnails (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/thumbnails |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/thumbnails (Get) |
| --- |

Description

Get file thumbnail

Gets the link to download a file thumbnail.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| version | (URI parameter) Version (required) | integer |
| Location | (Response) URI of file to download Member of RedirectResult model | URI |
| Request | (Response) An HttpRequestMessage; each HttpRequestMessage consists of: Version (Version object that consists of: Major Minor Build Revision MajorRevision MinorRevision ) Content (HttpContent object that consists of an array of headers) Method (HttpMethod object that consists of a method string) RequestUri (URI) Headers (Array of objects) Properties (Dictionary of string [key] and Object [value]) Member of RedirectResult model | HttpRequestMessage |

Response (application/json, text/json)

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
