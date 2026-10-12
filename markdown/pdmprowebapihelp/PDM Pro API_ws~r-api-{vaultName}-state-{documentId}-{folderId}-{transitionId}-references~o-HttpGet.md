---
title: "api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references (Get)"
project: ""
interface: "r-api-{vaultName}-state-{documentId}-{folderId}-{transitionId}-references"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-{documentId}-{folderId}-{transitionId}-references~o-HttpGet.html"
---

# api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > State Transition Resource Group : api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references (Get) |
| --- |

Description

GET: api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references Get all references

Gets all references for the specified file and transition.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| documentId | (URI parameter) Document ID (required) | integer |
| folderId | (URI parameter) Folder ID (required) | integer |
| transitionId | (URI parameter) Transition ID (required) | integer |
| File | (Response) A FileInfoConfigLess object that consists of: File (File object that consists of FileId (integer) and FileName (string) ) Folder (Folder object that consists of FolderId (integer) and FolderPath (string) ) Version Member of FileRefOfFileInfoConfigLess model | FileInfoConfigLess |
| IsToolbox | (Response) Whether in toolbox Member of FileRefOfFileInfoConfigLess model | integer |
| ObjectType | (Response) "File", "Folder", or "Bom" Member of FileRefOfFileInfoConfigLess model | String |

Response (application/json)

Array of FileRefOfFileInfoConfigLess objects

Response (text/json)

Array of FileRefOfFileInfoConfigLess objects

Response (application/xml)

Array of FileRefOfFileInfoConfigLess objects

Response (text/xml)

Array of FileRefOfFileInfoConfigLess objects

See Also

[State Transition Resource Group](PDM%20Pro%20API_ws~g-7b85dfc9-ca5f-4c42-8689-253a31d91dce.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
