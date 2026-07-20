---
title: "api/{vaultName}/checkin/buildtree/{changesetId} (Get)"
project: ""
interface: "r-api-{vaultName}-checkin-buildtree-{changesetId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-checkin-buildtree-{changesetId}~o-HttpGet.html"
---

# api/{vaultName}/checkin/buildtree/{changesetId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/checkin/buildtree/{changesetId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Stage Resource Group : api/{vaultName}/checkin/buildtree/{changesetId} (Get) |
| --- |

Description

GET: api/{vaultName}/checkin/buildtree/{changesetId} Get references tree

Builds a reference tree of files that are uploaded to the specified changeset.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| changesetId | (URI parameter) Changeset ID (required) | integer |
| File | (Response) A FileInfoStageModel object that consists of: File (File object that consists of FileId (integer) and FileName (string)) Folder (Folder object that consists of FolderId (integer) and FolderPath (string)) Version (integer) Quantity (integer) LockedBy (integer) NewVersion (boolean) DocumentType (DocumentType object that contains one of: NoObject = 0 NormalDocument = 1 VirtualComponent = 2 SavedBOM = 3 Item = 4 CutListItem = 5 ) LockViewId (globally unique identifier) LockProject (integer) ModifiedDate (date) | FileInfoStageModel |
| IsToolbox | (Response) 1 if a toolbox file, 0 if not | integer |
| ObjectType | (Response) "Folder", "File", or "Bom" | String |

Response (application/json)

Response (text/json)

Response (application/xml)

Response (text/xml)

Example

[Check in SOLIDWORKS Files in PDM Vault.postman_collection.json](Check%20in%20SOLIDWORKS%20Files%20%20in%20PDM%20Vault.postman_collection.json)

See Also

[Stage Resource Group](PDM%20Pro%20API_ws~g-ab7aa0c7-6261-4685-9682-f6301732b3ab.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
