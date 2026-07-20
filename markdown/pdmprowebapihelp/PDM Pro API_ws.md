---
title: "PDM Pro API Web Service"
project: ""
interface: ""
member: ""
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws.html"
---

# PDM Pro API Web Service

PDM Pro API Web Service

PDM Pro API Web Service

Spacing

Collapse All

Expand All

Description

The PDM Professional API Web Service consists GET, POST, PUT, PATCH, and DELETE HTTP requests that you call from your web client application. You must send the authenticate request before all others. See

[Getting Started](GettingStarted.html)

.

Authentication

| Post | api/{vaultName}/authenticate POST: api/{VaultName}/authenticate Use for the authenticate to get authentication token Authenticates the specified login for the specified vault and returns the authentication token and status. |
| --- | --- |

BOM

| Get | api/{vaultName}/bom/{bomDocumentId}/{version}/{folderId}/named GET: api/{VaultName}/bom/{BomDocumentId}/{Version}/{FolderID}/named Get named bom Gets the specified BOM. |
| --- | --- |
| Get | api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/computed?configId={configId}&latest={latest} GET: api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/weldmentcutlist or api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/computed Get computed BOM Gets the computed BOM. |
| Get | api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/weldmentcutlist?configId={configId}&latest={latest} GET: api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/weldmentcutlist or api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/computed Get computed BOM Gets the weldment cut list BOM. |

Configuration

| Get | api/{vaultName}/configuration/hooks/dll Retrieves the list of add-in hooks from the specified vault. |
| --- | --- |
| Put | api/{vaultName}/configuration/hooks/dll Puts add-in hook DLLs in the specified vault. |
| Delete | api/{vaultName}/configuration/hooks/dll Deletes add-in hook DLLs from the specified vault. |
| Get | api/{vaultName}/configuration/hooks/url Retrieves the list of webhooks configured in the specified vault. |
| Post | api/{vaultName}/configuration/hooks/url Sets the webhooks for the specified vault. |
| Get | api/configuration/fileserverroot GET: api/configuration/fileserverroot
Get file server root path(WebAPI storage)Gets the file server root path. |
| Post | api/configuration/fileserverroot POST: api/configuration/fileserverroot
Add file server root pathMigrates add-ins from previous file server root to the specified new one and reloads hooks instances. |
| Get | api/configuration/vaults?vaultName={vaultName} GET: api/configuration/vaults Get all vaults from the config file Gets all vaults from the vault configuration file. |

Data Card

| Post | api/{vaultName}/files/{fileId}/{folderId}/datacard Saves the data card for the specified file |
| --- | --- |
| Get | api/{vaultName}/files/{fileId}/{version}/datacard?folderId={folderId} GET: api/{VaultName}/files/{FileID}/{Version}/datacard Get file data card Gets the data card for the specified file, file version, and vault. |
| Post | api/{vaultName}/files/{fileId}/datacard?folderId={folderId} Saves the specified data card variables to the specified file. |
| Get | api/{vaultName}/folders/{folderId}/datacard GET: api/{VaultName}/folders/{FolderID}/datacard Get folder data card Gets the data card for the specified folder and vault. |

Default

| Get | api/{uri} Uses the specified URI to get information. |
| --- | --- |
| Post | api/{uri} Uses the specified URI to post information. |
| Put | api/{uri} Uses the specified URI to save information. |
| Patch | api/{uri} Uses the specified URI to patch information. |
| Delete | api/{uri} Uses the specified URI to delete information. |

File

| Get | api/{vaultName}/files/{fileId}/{folderId}/bominfo GET: api/{VaultName}/files/{FileID}/bominfo
Get file BOM infoGets the BOM information for the specified file. |
| --- | --- |
| Get | api/{vaultName}/files/{fileId}/{folderId}/history Gets a specified file's history. |
| Get | api/{vaultName}/files/{fileId}/{folderId}/moves Gets the history of moves for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{folderId}/versions GET: api/{VaultName}/files/{FileID}/versions Get file version info Gets the specified file's version information. |
| Delete | api/{vaultName}/files/{fileId}/{folderId}?destroy={destroy} Deletes the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{configId}/{folderId}/whereused?anyVersion={anyVersion} GET: api/{VaultName}/files/{FileID}/{Version}/whereused
Get file where usedGets the parent files where the specified file is used. |
| Get | api/{vaultName}/files/{fileId}/{version}/{configId}/whereused?folderId={folderId}&anyVersion={anyVersion} GET: api/{VaultName}/files/{FileID}/{Version}/whereused
Get file where usedGets the parent files where the specified file is used. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId} Gets information about the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/ActiveConfig Gets the active configuration for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/allreferences?configId={configId}&includeSubParents={includeSubParents} GET: api/{VaultName}/files/{FileID}/{Version}/allreferences Get all file references Gets the reference tree of the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/configurations Gets the configurations for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/download Gets the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/info Gets information about the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/info/extended Gets extended version information for a specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/references?configId={configId} GET: api/{VaultName}/files/{FileID}/{Version}/references Get file references Gets the top level file references of the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/thumbnails Gets a specified file's thumbnail. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/transitions Gets the file transitions for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/variables Gets configuration variable information for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/ActiveConfig?folderId={folderId} Gets the active configuration for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/allreferences?configId={configId}&folderId={folderId}&includeSubParents={includeSubParents} GET: api/{VaultName}/files/{FileID}/{Version}/allreferences Get all file references Gets the reference tree of the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/configurations?folderId={folderId} Gets the configurations for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/download?folderId={folderId} Gets the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/info/extended?folderId={folderId} Gets extended version information for a specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/info?folderId={folderId} Gets information about the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/references?configId={configId}&folderId={folderId} GET: api/{VaultName}/files/{FileID}/{Version}/references Get file references Gets the top level file references of the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/thumbnails?folderId={folderId} Gets a specified file's thumbnail. |
| Get | api/{vaultName}/files/{fileId}/{version}/transitions?folderId={folderId} Gets the file transitions for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/variables?folderId={folderId} Gets configuration variable information for the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}/whereused?configId={configId}&folderId={folderId}&anyVersion={anyVersion} GET: api/{VaultName}/files/{FileID}/{Version}/whereused Get file where used Gets the parents of the specified file. |
| Get | api/{vaultName}/files/{fileId}/{version}?folderId={folderId} Gets information about the specified file. |
| Get | api/{vaultName}/files/{fileId}/bominfo?folderId={folderId} GET: api/{VaultName}/files/{FileID}/bominfo Get file BOM info Gets the BOM information for the specified file. |
| Get | api/{vaultName}/files/{fileId}/history?folderId={folderId} Gets a specified file's history. |
| Get | api/{vaultName}/files/{fileId}/info?version={version}&folderId={folderId} Gets information about the specified file. |
| Get | api/{vaultName}/files/{fileId}/moves?folderId={folderId} Gets the history of moves for the specified file. |
| Get | api/{vaultName}/files/{fileId}/transitions?version={version}&folderId={folderId} Gets the file transitions for the specified file. |
| Get | api/{vaultName}/files/{fileId}/versions?folderId={folderId} GET: api/{VaultName}/files/{FileID}/versions Get file version info Gets the specified file's version information. |
| Delete | api/{vaultName}/files/{fileId}?folderId={folderId}&destroy={destroy} Deletes the specified file. |
| Get | api/{vaultName}/files/{fileId}?version={version}&folderId={folderId} Gets information about the specified file. |
| Post | api/{vaultName}/files/buildtree/checkout POST: api/{VaultName}/files/buildtree/checkout Build checkout references tree Gets the tree of references in the specified file's checkout. |
| Post | api/{vaultName}/files/buildtree/undo POST: api/{VaultName}/files/buildtree/undo Build undo checkout references tree Builds the reference tree to undo the checkout of the specified file. |
| Post | api/{vaultName}/files/CheckOut POST: api/{VaultName}/files/CheckOut Lock file Checks out the specified file(s). |
| Post | api/{vaultName}/files/info POST: api/{VaultName}/files/info Gets information about the specified files. |
| Post | api/{vaultName}/files/infofrompath Gets information about a file in the specified vault. |
| Post | api/{vaultName}/files/UndoCheckOut POST: api/{VaultName}/files/UndoCheckOut Undo lock file Unlocks the specified file. |

Folder

| Get | api/{vaultName}/folders/{folderId} GET: api/{VaultName}/folders/{FolderID} or api/{VaultName}/folders/{FolderID}/info Get folder info Gets information for the specified folder. |
| --- | --- |
| Get | api/{vaultName}/folders/{folderId}/browse GET: api/{VaultName}/folders/{FolderID}/browse Get browse folder Gets the files and folders in the specified folder. |
| Get | api/{vaultName}/folders/{folderId}/info GET: api/{VaultName}/folders/{FolderID} or api/{VaultName}/folders/{FolderID}/info Get folder info Gets information for the specified folder. |
| Delete | api/{vaultName}/folders/{folderId}?destroy={destroy} DELETE: api/{VaultName}/folders/{FolderID} Delete folder Deletes the specified folder. |
| Put | api/{vaultName}/folders/{parentFolderId} PUT: api/{VaultName}/folders/{ParentFolderID} Add folder Adds a folder to the specified folder. |
| Post | api/{vaultName}/folders/info POST: api/{VaultName}/folders/info Get folder info Gets information about specified folders in the specified vault. |

Group

| Get | api/{vaultName}/groups GET: api/{VaultName}/groups or api/{VaultName}/groups/all Get groups Gets the groups in the specified vault. |
| --- | --- |
| Get | api/{vaultName}/groups/{groupId} GET: api/{VaultName}/groups/{GroupID} or api/{VaultName}/groups/{GroupID}/info Get group info Gets information about the specified group. |
| Get | api/{vaultName}/groups/{groupId}/info GET: api/{VaultName}/groups/{GroupID} or api/{VaultName}/groups/{GroupID}/info Get group info Gets information about the specified group. |
| Get | api/{vaultName}/groups/all GET: api/{VaultName}/groups or api/{VaultName}/groups/all Get groups Gets the groups in the specified vault. |

Notification

| Post | api/{vaultName}/notifications POST: api/{VaultName}/notifications Send message Sends the specified message. |
| --- | --- |
| Post | api/{vaultName}/notifications/markRead POST: api/{vaultName}/notifications/markRead Mark message as read Marks a notification as read. |
| Get | api/{vaultName}/notifications?all={all}&pageNo={pageNo}&pageSize={pageSize} GET: api/{VaultName}/notifications Get user notifications Gets the user notifications. |

Progress

| Get | api/{vaultName}/progress/{guid}/result GET: api/{vaultName}/progress/{guid}/result Gets the result of the specified operation. |
| --- | --- |
| Get | api/{vaultName}/progress/{guid}/status GET: api/{vaultName}/progress/{guid}/status Get operation status Gets the status of the specified operation. |

Stage

| Get | api/{vaultName}/changeset/create GET: api/{vaultName}/changeset/create Generate changesetId Gets a changeset ID for the specified vault. |
| --- | --- |
| Put | api/{vaultName}/checkin/{changesetId}/{overrideVersion} PUT: api/{vaultName}/checkin/{changesetId}/{overrideVersion=false} Check in files from the changeset Checks in the specified changeset. |
| Put | api/{vaultName}/checkin/addfiles/{changesetId} PUT: api/{vaultname}/checkin/addfiles/{changesetId=0} Upload files or document ids to changeset to the check in operation Adds files to a changeset for checkin. (See Remarks ) |
| Get | api/{vaultName}/checkin/buildtree/{changesetId} GET: api/{vaultName}/checkin/buildtree/{changesetId} Get references tree Builds a reference tree of files that are uploaded to the specified changeset. |
| Put | api/{vaultName}/files/{changesetId}/finishadd PUT: api/{vaultName}/files/{changesetId}/finishadd Finish of add file operation. This method adds files from changeset to the vault. Adds files in the specified changeset to the vault. (See Remarks ) |
| Put | api/{vaultName}/files/{changesetId}/upload PUT: api/{vaultname}/files/{changesetId}/upload Upload file to changeset to add files operations Uploads files to the specified changeset. (See Remarks ) |
| Put | api/stage/{vaultName}/{documentId}?folderId={folderId}&overrideVersion={overrideVersion} Checks in the specified document. |

State Transition

| Get | api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references GET: api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references Get all references Gets all references for the specified file and transition. |
| --- | --- |
| Get | api/{vaultName}/state/{documentId}/{folderId}/transitions Gets the transitions available for the specified file. |
| Get | api/{vaultName}/state/{documentId}/transitions?folderId={folderId} Gets the transitions available for the specified file. |
| Get | api/{vaultName}/state/{transitionId} GET: api/{vaultName}/state/{transitionId} Get transition info Gets information about the specified transition. |
| Post | api/{vaultName}/state/{transitionId}/changestate?revoke={revoke} POST: api/{vaultName}/state/{transitionId}/changestate Change state Changes the state of the specified documents. |
| Post | api/{vaultName}/state/{transitionId}/DynamicNotificationUsers POST: api/{vaultName}/state/{transitionId}/DynamicNotificationUsers Get dynamic notification users Gets the users to notify when the specified items undergo the specified transition. |
| Post | api/{vaultName}/state/{transitionId}/HistoryComments POST: api/{vaultName}/state/{transitionId}/HistoryComments Get transition comment history for multiple files Gets the comment histories for specified files that undergo the specified transition. |
| Post | api/{vaultName}/state/transitions POST: api/{vaultName}/state/transitions Get available transitions for multiple files Gets the transitions available for multiple files. |

User

| Get | api/{vaultName}/users GET: api/{VaultName}/users or api/{VaultName}/users/all Get users Gets the users of the specified vault. |
| --- | --- |
| Get | api/{vaultName}/users/{userId} GET: api/{VaultName}/users/{UserID} or api/{VaultName}/users/{UserID}/info Get user info Gets information about the specified user. |
| Get | api/{vaultName}/users/{userId}/Extended GET: api/{VaultName}/users/{UserID}/Extended Get user info extended Gets extended information about the specified user. |
| Put | api/{vaultName}/users/{userId}/Extended PUT: api/{VaultName}/users/{UserID}/Extended Set user info extended Saves information about the specified user. |
| Get | api/{vaultName}/users/{userId}/info GET: api/{VaultName}/users/{UserID} or api/{VaultName}/users/{UserID}/info Get user info Gets information about the specified user. |
| Get | api/{vaultName}/users/{userId}/Picture GET: api/{VaultName}/users/{UserID}/Picture Get user picture Gets the picture of the specified user. |
| Put | api/{vaultName}/users/{userId}/Picture PUT: api/{VaultName}/users/{UserID}/Picture Put user picture Saves the picture of the specified user. |
| Delete | api/{vaultName}/users/{userId}/Picture DELETE: api/{VaultName}/users/{UserID}/Picture Delete user picture Deletes the picture of the specified user. |
| Get | api/{vaultName}/users/all GET: api/{VaultName}/users or api/{VaultName}/users/all Get users Gets the users of the specified vault. |

Vault

| Get | api/{vaultName} GET: api/{VaultName} or api/{VaultName}/info Get vault properties Gets the properties of the specified vault. |
| --- | --- |
| Post | api/{vaultName}/delete/computetree POST: api/{VaultName}/delete/computetree Delete compute tree Deletes the specified items in the specified vault. |
| Get | api/{vaultName}/info GET: api/{VaultName} or api/{VaultName}/info Get vault properties Gets the properties of the specified vault. |

Version

| Get | api/version/webapi GET: api/version/webapi Get version Gets the version of this web application. |
| --- | --- |

Workflow

| Get | api/{vaultName}/workflows GET: api/{VaultName}/workflows Get workflows Gets the workflows in the specified vault. |
| --- | --- |
| Get | api/{vaultName}/workflows/icons GET: api/{vaultName}/workflows/icons Get state icons Gets the workflow state icons in the specified vault. |

Search

| Get | api/{vaultName}/search Gets objects in the specified vault. |
| --- | --- |
| Post | api/{vaultName}/search Gets objects in the vault that contain the specified string. |
| Post | api/{vaultName}/searchvariables Specifies parameters and variables for a search. |
