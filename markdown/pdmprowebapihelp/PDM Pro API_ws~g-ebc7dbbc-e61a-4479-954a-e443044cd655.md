---
title: "Folder Resource Group"
project: ""
interface: "g-ebc7dbbc-e61a-4479-954a-e443044cd655"
member: ""
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~g-ebc7dbbc-e61a-4479-954a-e443044cd655.html"
---

# Folder Resource Group

PDM Pro API Web Service

Folder Resource Group

Spacing

Collapse All

Expand All

| PDM Pro API Web Service : Folder Resource Group |
| --- |

Description

Folder services. You must send

[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-authenticate~o-HttpPost.html)

before calling these. See

[Getting Started](GettingStarted.html)

.

Operations

| Get | api/{vaultName}/folders/{folderId} GET: api/{VaultName}/folders/{FolderID} or api/{VaultName}/folders/{FolderID}/info Get folder info Gets information for the specified folder. |
| --- | --- |
| Get | api/{vaultName}/folders/{folderId}/browse GET: api/{VaultName}/folders/{FolderID}/browse Get browse folder Gets the files and folders in the specified folder. |
| Get | api/{vaultName}/folders/{folderId}/info GET: api/{VaultName}/folders/{FolderID} or api/{VaultName}/folders/{FolderID}/info Get folder info Gets information for the specified folder. |
| Delete | api/{vaultName}/folders/{folderId}?destroy={destroy} DELETE: api/{VaultName}/folders/{FolderID} Delete folder Deletes the specified folder. |
| Put | api/{vaultName}/folders/{parentFolderId} PUT: api/{VaultName}/folders/{ParentFolderID} Add folder Adds a folder to the specified folder. |
| Post | api/{vaultName}/folders/info POST: api/{VaultName}/folders/info Get folder info Gets information about specified folders in the specified vault. |

See Also

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
