---
title: "api/{vaultName}/files/{fileId}/{version}/{folderId}/thumbnails (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-{folderId}-thumbnails"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-{folderId}-thumbnails~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/{folderId}/thumbnails (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/thumbnails |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/{folderId}/thumbnails (Get) |
| --- |

Description

Gets a specified file's thumbnail.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| version | (Required URI Parameter) File version | integer |
| folderId | (URI Parameter) Folder ID, default is 0 | integer |
| Location | (Response) URI location (Member of RedirectResult Model) | URI |
| Request | (Response) HttpRequestMessage: Version: Major: integer Minor: integer Build: integer Revision: integer MajorRevision: integer MinorRevision: integer Content: HttpContent: collection of Headers Method HttpMethod: string RequestUri: URI Headers: array Properties: Dictionary of key/value pairs (Member of RedirectResult Model) | HttpRequestMessage |

Response (application/json, text/json)

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
