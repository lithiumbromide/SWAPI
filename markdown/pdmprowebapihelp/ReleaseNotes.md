---
title: "Release Notes"
project: "PDM Pro Web API Help"
interface: ""
member: ""
kind: "topic"
source: "pdmprowebapihelp/ReleaseNotes.html"
---

# Release Notes

- [SOLIDWORKS PDM Professional 2025 Web Api](#2025)
- [SOLIDWORKS PDM Professional 2024 Web API](#2024)
- [SOLIDWORKS PDM Professional 2023 Web API](#2023)
- [SOLIDWORKS PDM Professional 2022 Web API](#2022)

##### SOLIDWORKS PDM Professional 2025 Web API

###### Configuration

- [api/configuration/fileserverroot](PDM%20Pro%20API_ws~r-api-configuration-fileserverroot~o-HttpGet.html)

  (Get)
- [api/configuration/fileserverroot](PDM%20Pro%20API_ws~r-api-configuration-fileserverroot~o-HttpPost.html)

  (Post)
- [api/{vaultName}/configuration/hooks/dll](PDM%20Pro%20API_ws~r-api-{vaultName}-configuration-hooks-dll~o-HttpGet.html)

  (Get)
- [api/{vaultName}/configuration/hooks/dll](PDM%20Pro%20API_ws~r-api-{vaultName}-configuration-hooks-dll~o-HttpPut.html)

  (Put)
- [api/{vaultName}/configuration/hooks/dll](PDM%20Pro%20API_ws~r-api-{vaultName}-configuration-hooks-dll~o-HttpDelete.html)

  (Delete)
- [api/{vaultName}/configuration/hooks/url](PDM%20Pro%20API_ws~r-api-{vaultName}-configuration-hooks-url~o-HttpGet.html)

  (Get)
- [api/{vaultName}/configuration/hooks/url](PDM%20Pro%20API_ws~r-api-{vaultName}-configuration-hooks-url~o-HttpPost.html)

  (Post)

##### SOLIDWORKS PDM Professional 2024 Web API

###### Data Card

- [api/{vaultName}/files/{fileId}/{folderId}/datacard](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7BfolderId%7D-datacard~o-HttpPost.html)

  (Post)

- [api/{vaultName}/files/{fileId}/datacard?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-datacard-folderId=%7BfolderId%7D~o-HttpPost.html)

  (Post)

###### File

- [api/{vaultName}/files/{fileId}?folderId={folderId}&destroy={destroy}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-folderId=%7BfolderId%7D-destroy=%7Bdestroy%7D~o-HttpDelete.html)

  (Delete)
- [api/{vaultName}/files/{fileId}/{folderId}?destroy={destroy}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7BfolderId%7D-destroy=%7Bdestroy%7D~o-HttpDelete.html)

  (Delete)
- [api/{vaultName}/files/{fileId}/{version}/configurations?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-configurations-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/configurations](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-configurations~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/info/extended?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-info-extended-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/info/extended](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-info-extended~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/ActiveConfig?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-ActiveConfig-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/ActiveConfig](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-ActiveConfig~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/variables?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-variables-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/variables](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-variables~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{folderId}/versions](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7BfolderId%7D-versions~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/allreferences?configId={configId}&includeSubParents={includeSubParents}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-allreferences-configId=%7BconfigId%7D-includeSubParents=%7BincludeSubParents%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/references?configId={configId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-references-configId=%7BconfigId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}?version={version}&folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-version=%7Bversion%7D-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/info?version={version}&folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-info-version=%7Bversion%7D-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/info?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-info-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/info](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-info~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/transitions?version={version}&folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-transitions-version=%7Bversion%7D-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/transitions?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-transitions-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/transitions](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-transitions~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/moves?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-moves-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{folderId}/moves](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7BfolderId%7D-moves~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/history?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-history-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{folderId}/history](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7BfolderId%7D-history~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{configId}/whereused?folderId={folderId}&anyVersion={anyVersion}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BconfigId%7D-whereused-folderId=%7BfolderId%7D-anyVersion=%7BanyVersion%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{configId}/{folderId}/whereused?anyVersion={anyVersion}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BconfigId%7D-%7BfolderId%7D-whereused-anyVersion=%7BanyVersion%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{folderId}/bominfo](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7BfolderId%7D-bominfo~o-HttpGet.html)

  (Get)
- PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7BfolderId%7D-bominfo~o-HttpGet.html

  [api/{vaultName}/files/{fileId}/{version}/download?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-download-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/download](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-download~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/thumbnails?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-thumbnails-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/files/{fileId}/{version}/{folderId}/thumbnails](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-files-%7BfileId%7D-%7Bversion%7D-%7BfolderId%7D-thumbnails~o-HttpGet.html)

  (Get)

###### Search

- [api/{vaultName}/search (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-search~o-HttpGet.html)
- [api/{vaultName}/search (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-search~o-HttpPost.html)
- [api/{vaultName}/searchvariables (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-searchvariables~o-HttpPost.html)

###### Stage

- [api/stage/{vaultName}/{documentId}?folderId={folderId}&overrideVersion={overrideVersion}](PDM%20Pro%20API_ws~r-api-stage-%7BvaultName%7D-%7BdocumentId%7D-folderId=%7BfolderId%7D-overrideVersion=%7BoverrideVersion%7D~o-HttpPut.html)

  (Post)

###### State Transition

- [api/{vaultName}/state/{documentId}/transitions?folderId={folderId}](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-state-%7BdocumentId%7D-transitions-folderId=%7BfolderId%7D~o-HttpGet.html)

  (Get)
- [api/{vaultName}/state/{documentId}/{folderId}/transitions](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-state-%7BdocumentId%7D-%7BfolderId%7D-transitions~o-HttpGet.html)

  (Get)

##### SOLIDWORKS PDM Professional 2023 Web API

###### File

- [api/{vaultName}/files/infofrompath (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-infofrompath~o-HttpPost.html)

##### SOLIDWORKS PDM Professional 2022 Web API

###### Authentication

- [api/{vaultName}/authenticate (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html)

###### BOM

- [api/{vaultName}/bom/{bomDocumentId}/{version}/{folderId}/named (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-bom-{bomDocumentId}-{version}-{folderId}-named~o-HttpGet.html)
- [api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/computed?configId={configId}&latest={latest} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-bom-{bomTypeId}-{fileId}-{version}-{folderId}-computed-configId={configId}-latest={latest}~o-HttpGet.html)
- [api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/weldmentcutlist?configId={configId}&latest={latest} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-bom-{bomTypeId}-{fileId}-{version}-{folderId}-weldmentcutlist-configId={configId}-latest={latest}~o-HttpGet.html)

###### Configuration

- [api/configuration/vaults?vaultName={vaultName} (Get)](PDM%20Pro%20API_ws~r-api-configuration-vaults-vaultName={vaultName}~o-HttpGet.html)

###### Data Card

- [api/{vaultName}/files/{fileId}/{version}/datacard?folderId={folderId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-datacard-folderId={folderId}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/datacard (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-datacard~o-HttpPost.html)
- [api/{vaultName}/folders/{folderId}/datacard (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-folders-{folderId}-datacard~o-HttpGet.html)

###### Default

- [api/{uri} (Get)](PDM%20Pro%20API_ws~r-api-{uri}~o-HttpGet.html)
- [api/{uri} (Post)](PDM%20Pro%20API_ws~r-api-{uri}~o-HttpPost.html)
- [api/{uri} (Put)](PDM%20Pro%20API_ws~r-api-{uri}~o-HttpPut.html)
- [api/{uri} (Patch)](PDM%20Pro%20API_ws~r-api-{uri}~o-HttpPatch.html)
- [api/{uri} (Delete)](PDM%20Pro%20API_ws~r-api-{uri}~o-HttpDelete.html)

###### File

- [api/{vaultName}/files/{fileId}/{version} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/ActiveConfig (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-ActiveConfig~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/allreferences?configId={configId}&folderId={folderId}&includeSubParents={includeSubParents} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-allreferences-configId={configId}-folderId={folderId}-includeSubParents={includeSubParents}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/configurations (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-configurations~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/download (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-download~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/info (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-info~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/info/extended (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-info-extended~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/references?configId={configId}&folderId={folderId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-references-configId={configId}-folderId={folderId}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/thumbnails (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-thumbnails~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/variables (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-variables~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/{version}/whereused?configId={configId}&folderId={folderId}&anyVersion={anyVersion} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-{version}-whereused-configId={configId}-folderId={folderId}-anyVersion={anyVersion}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/bominfo?folderId={folderId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-bominfo-folderId={folderId}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/info?version={version} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-info-version={version}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/transitions?version={version} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-transitions-version={version}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}/versions?folderId={folderId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-versions-folderId={folderId}~o-HttpGet.html)
- [api/{vaultName}/files/{fileId}?destroy={destroy} (Delete)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-destroy={destroy}~o-HttpDelete.html)
- [api/{vaultName}/files/{fileId}?version={version} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{fileId}-version={version}~o-HttpGet.html)
- [api/{vaultName}/files/buildtree/checkout (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-buildtree-checkout~o-HttpPost.html)
- [api/{vaultName}/files/buildtree/undo (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-buildtree-undo~o-HttpPost.html)
- [api/{vaultName}/files/CheckOut (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-CheckOut~o-HttpPost.html)
- [api/{vaultName}/files/info (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-info~o-HttpPost.html)
- [api/{vaultName}/files/UndoCheckOut (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-UndoCheckOut~o-HttpPost.html)

###### Folder

- [api/{vaultName}/folders/{folderId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-folders-{folderId}~o-HttpGet.html)
- [api/{vaultName}/folders/{folderId}/browse (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-folders-{folderId}-browse~o-HttpGet.html)
- [api/{vaultName}/folders/{folderId}/info (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-folders-info~o-HttpPost.html)
- [api/{vaultName}/folders/{folderId}?destroy={destroy} (Delete)](PDM%20Pro%20API_ws~r-api-{vaultName}-folders-{folderId}-destroy={destroy}~o-HttpDelete.html)
- [api/{vaultName}/folders/{parentFolderId} (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-folders-{folderId}~o-HttpGet.html)
- [api/{vaultName}/folders/info (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-folders-info~o-HttpPost.html)

###### Group

- [api/{vaultName}/groups (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-groups~o-HttpGet.html)
- [api/{vaultName}/groups/{groupId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-groups-{groupId}~o-HttpGet.html)
- [api/{vaultName}/groups/{groupId}/info (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-groups-{groupId}-info~o-HttpGet.html)
- [api/{vaultName}/groups/all (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-groups-all~o-HttpGet.html)

###### Notification

- [api/{vaultName}/notifications (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-notifications~o-HttpPost.html)
- [api/{vaultName}/notifications/markRead (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-notifications-markRead~o-HttpPost.html)
- [api/{vaultName}/notifications?all={all}&pageNo={pageNo}&pageSize={pageSize} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-notifications-all={all}-pageNo={pageNo}-pageSize={pageSize}~o-HttpGet.html)

###### Progress

- [api/{vaultName}/progress/{guid}/result (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-progress-{guid}-result~o-HttpGet.html)
- [api/{vaultName}/progress/{guid}/status (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-progress-{guid}-status~o-HttpGet.html)

###### Stage

- [api/{vaultName}/changeset/create (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-changeset-create~o-HttpGet.html)
- [api/{vaultName}/checkin/{changesetId}/{overrideVersion} (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-checkin-{changesetId}-{overrideVersion}~o-HttpPut.html)
- [api/{vaultName}/checkin/addfiles/{changesetId} (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-checkin-addfiles-{changesetId}~o-HttpPut.html)
- [api/{vaultName}/checkin/buildtree/{changesetId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-checkin-buildtree-{changesetId}~o-HttpGet.html)
- [api/{vaultName}/files/{changesetId}/finishadd (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{changesetId}-finishadd~o-HttpPut.html)
- [api/{vaultName}/files/{changesetId}/upload (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{changesetId}-upload~o-HttpPut.html)

###### State Transition

- [api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-state-{documentId}-{folderId}-{transitionId}-references~o-HttpGet.html)
- [api/{vaultName}/state/{documentId}/transitions (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-state-{documentId}-transitions~o-HttpGet.html)
- [api/{vaultName}/state/{transitionId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-state-{transitionId}~o-HttpGet.html)
- [api/{vaultName}/state/{transitionId}/changestate?revoke={revoke} (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-state-{transitionId}-changestate-revoke={revoke}~o-HttpPost.html)
- [api/{vaultName}/state/{transitionId}/DynamicNotificationUsers (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-state-{transitionId}-DynamicNotificationUsers~o-HttpPost.html)
- [api/{vaultName}/state/{transitionId}/HistoryComments (Post](PDM%20Pro%20API_ws~r-api-{vaultName}-state-{transitionId}-HistoryComments~o-HttpPost.html)

  )
- [api/{vaultName}/state/transitions (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-state-transitions~o-HttpPost.html)

###### User

- [api/{vaultName}/users (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-users~o-HttpGet.html)
- [api/{vaultName}/users/{userId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-users-{userId}~o-HttpGet.html)
- [api/{vaultName}/users/{userId}/Extended (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-users-{userId}-Extended~o-HttpGet.html)
- [api/{vaultName}/users/{userId}/Extended (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-users-{userId}-Extended~o-HttpPut.html)
- [api/{vaultName}/users/{userId}/info (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-users-{userId}-info~o-HttpGet.html)
- [api/{vaultName}/users/{userId}/Picture (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-users-{userId}-Picture~o-HttpGet.html)
- [api/{vaultName}/users/{userId}/Picture (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-users-{userId}-Picture~o-HttpPut.html)
- [api/{vaultName}/users/{userId}/Picture (Delete)](PDM%20Pro%20API_ws~r-api-{vaultName}-users-{userId}-Picture~o-HttpDelete.html)
- [api/{vaultName}/users/all (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-users-all~o-HttpGet.html)

###### Vault

- [api/{vaultName} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}~o-HttpGet.html)
- [api/{vaultName}/delete/computetree (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-delete-computetree~o-HttpPost.html)
- [api/{vaultName}/info (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-info~o-HttpGet.html)
- [api/{vaultName}/search (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-search~o-HttpGet.html)
- [api/{vaultName}/search (Post)](PDM%20Pro%20API_ws~r-api-{vaultName}-search~o-HttpPost.html)

###### Version

- [api/version/webapi (Get)](PDM%20Pro%20API_ws~r-api-version-webapi~o-HttpGet.html)

###### Workflow

- [api/{vaultName}/workflows (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-workflows~o-HttpGet.html)
- [api/{vaultName}/workflows/icons (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-workflows-icons~o-HttpGet.html)
