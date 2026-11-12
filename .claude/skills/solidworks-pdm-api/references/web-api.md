# PDM Professional Web API
## Contents
- [Server prerequisites](#server-prerequisites)
- [Authentication](#authentication)
- [Route groups](#route-groups)
- [Flows](#flows)
- [Web event hooks](#web-event-hooks)
- [Sources](#sources)
## Server prerequisites
- The Web API is a REST service (ASP.NET Web API on IIS) installed with the SOLIDWORKS PDM Web API Server, PDM Professional only. In the Administration tool add the Web API server, add the vault to it and configure the vault; routes are then served under `http://host:port/api/`.
- Browser clients from another origin need CORS: install the IIS CORS module, add a `<cors enabled='true'>` block to the `web.config` of the Web API site (for example in `C:\inetpub\wwwroot\SOLIDWORKSPDM\WebApi`), then restart the SOLIDWORKS PDM WebAPI application pool and the SWPDMWebAPI site. Server-side clients (Node, Python, C#) do not need CORS.
- When one machine is both Web API server and client, staging files for check-in may require the SOLIDWORKS PDM WebAPI application pool identity to be the logged-in Windows account.
- `GET api/version/webapi` returns the product and file version of the server.
## Authentication
`POST api/{vaultName}/authenticate` with JSON body `{"Username": "...", "Password": "..."}` and `Content-Type: application/json`. The response JSON carries the token in `JwtString`; send `Authorization: Bearer <JwtString>` with every other request. Keep credentials out of source code (environment variables or a secret store).
## Route groups
All routes start with `api/{vaultName}/` unless noted. IDs (`fileId`, `folderId`, `version`, `configId`, `transitionId`) come from browse, search or info responses; the root folder ID is 1; `ObjectType` is Folder 0, File 1, Bom 3.
| Group | Routes |
| --- | --- |
| Folders | `GET folders/{folderId}/browse` (files and subfolders with Id, Name, Version, State, StateId, Path), `GET folders/{folderId}/info`, `GET folders/{folderId}/datacard`, `PUT folders/{parentFolderId}` (create), `DELETE folders/{folderId}?destroy={destroy}` |
| Files | `POST files/infofrompath` (body: path relative to the vault root as a JSON string), `POST files/info`; per version and folder `GET files/{fileId}/{version}/{folderId}` plus `/info`, `/info/extended`, `/configurations`, `/ActiveConfig`, `/variables` (card values per configuration), `/references?configId=`, `/allreferences?configId=&includeSubParents=`, `/thumbnails`, `/transitions` and `/download`; per folder without a version `GET files/{fileId}/{folderId}/versions`, `/history`, `/moves` and `/bominfo`; where-used `GET files/{fileId}/{version}/{configId}/{folderId}/whereused?anyVersion=`; `DELETE files/{fileId}/{folderId}?destroy={destroy}`. Most routes also exist with `folderId` as a query parameter instead of a path segment |
| Check-out | `POST files/CheckOut` and `POST files/UndoCheckOut` (body: array of `{FileId, FolderId}`; response `IsSuccess` and `Warning` per file), `POST files/buildtree/checkout`, `POST files/buildtree/undo` |
| Data card | read with `GET files/{fileId}/{version}/datacard?folderId=` or `.../variables`; save with `POST files/{fileId}/{folderId}/datacard` or `POST files/{fileId}/datacard?folderId=` (body: array of `{Models: [{VarId, VarName, VarValue, VarType, ...}], ConfigurationName, ConfigurationId}`) |
| Stage and check-in | `GET changeset/create`, `PUT files/{changesetId}/upload` (binary body), `PUT files/{changesetId}/finishadd`, `PUT checkin/addfiles/{changesetId}` (call with 0, returns a new changeset ID), `GET checkin/buildtree/{changesetId}`, `PUT checkin/{changesetId}/{overrideVersion}` (body: `DocumentIds`, `Comments`) |
| Progress | `GET progress/{guid}/status` and `GET progress/{guid}/result` for the GUID returned by `finishadd` and `checkin` |
| Search | `POST search` (body: a JSON string to find), `GET search`, `POST searchvariables` |
| Workflow | `GET state/{documentId}/transitions`, `GET state/{transitionId}`, `POST state/{transitionId}/changestate?revoke={revoke}` (body: `Documents`, `Comment`, `NotificationComment`, `NotifyUsers`, `Password`), `POST state/transitions`, `GET workflows` |
| BOM | `GET bom/{bomTypeId}/{fileId}/{version}/{folderId}/computed?configId=&latest=`, `.../weldmentcutlist`, `GET bom/{bomDocumentId}/{version}/{folderId}/named`, `GET files/{fileId}/{folderId}/bominfo` |
| Users and groups | `GET users`, `GET users/all`, `GET users/{userId}/info`, `GET groups`, `GET groups/{groupId}/info` |
| Notifications | `GET notifications?all=&pageNo=&pageSize=`, `POST notifications`, `POST notifications/markRead` |
| Configuration (2025) | `GET/PUT/DELETE configuration/hooks/dll`, `GET/POST configuration/hooks/url`, and outside a vault `GET/POST api/configuration/fileserverroot` |
## Flows
- Download the latest version: `POST files/infofrompath` (or `browse`, or `search`) to get `Id`, `Version` and `ParentFolderId`, then `GET files/{fileId}/{version}/{folderId}/download`.
- Add new files: `GET changeset/create`, `PUT files/{changesetId}/upload` with the file bytes, `PUT files/{changesetId}/finishadd`, then poll `progress/{guid}/status` and read `progress/{guid}/result`.
- Edit card values: `POST files/CheckOut`, `POST files/{fileId}/{folderId}/datacard` with the changed `VarId`/`VarValue` per configuration (read IDs first from `.../variables` or the data card route), `PUT checkin/addfiles/0` with the file to obtain a changeset ID (the official sample calls `changeset/create` first), `PUT checkin/{changesetId}/false` with the document IDs and a comment, then poll progress.
- Change state: `GET state/{documentId}/transitions` to find the `TransitionId` (check `MustEnterComments`), then `POST state/{transitionId}/changestate?revoke=false` with the document IDs; each result has `IsSuccess` and a `Warning`.
## Web event hooks
Since 2025 the Web API raises 18 pre and post events for operations performed through it (add folder, add files, get, check out, undo check-out, check-in, change state, delete file, delete folder). Webhooks are URLs registered per vault with `configuration/hooks/url` that receive an HTTP POST with the event payload; returning status 402 or 412 cancels the operation. Add-in hooks are DLLs implementing `IAddInHook.OnCmd`, uploaded with `configuration/hooks/dll`. They fire for the listed Web API requests only; desktop clients still need `IEdmAddIn5` hooks.
## Sources
- `markdown/pdmprowebapihelp/GettingStarted.md`
- `markdown/pdmprowebapihelp/index.md`
- `markdown/pdmprowebapihelp/ModifyDatacard.md`
- `markdown/pdmprowebapihelp/Welcome.md`
- `markdown/pdmprowebapihelp/ReleaseNotes.md`
- `markdown/pdmprowebapihelp/PDMProWebAPI_Webhooks_Programming_Guide.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-authenticate~o-HttpPost.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-folders-{folderId}-browse~o-HttpGet.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-infofrompath~o-HttpPost.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-{folderId}-download~o-HttpGet.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-{folderId}-variables~o-HttpGet.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-CheckOut~o-HttpPost.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-datacard~o-HttpPost.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-changeset-create~o-HttpGet.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{changesetId}-upload~o-HttpPut.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{changesetId}-finishadd~o-HttpPut.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-checkin-addfiles-{changesetId}~o-HttpPut.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-checkin-{changesetId}-{overrideVersion}~o-HttpPut.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-progress-{guid}-status~o-HttpGet.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-{documentId}-transitions~o-HttpGet.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-{transitionId}-changestate-revoke={revoke}~o-HttpPost.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-search~o-HttpPost.md`
- `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-version-webapi~o-HttpGet.md`
