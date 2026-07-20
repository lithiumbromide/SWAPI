---
title: "State Transition Resource Group"
project: ""
interface: "g-7b85dfc9-ca5f-4c42-8689-253a31d91dce"
member: ""
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~g-7b85dfc9-ca5f-4c42-8689-253a31d91dce.html"
---

# State Transition Resource Group

PDM Pro API Web Service

State Transition Resource Group

Spacing

Collapse All

Expand All

| PDM Pro API Web Service : State Transition Resource Group |
| --- |

Description

State transition services. You must send

[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-authenticate~o-HttpPost.html)

before calling these. See

[Getting Started](GettingStarted.html)

.

Operations

| Get | api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references GET: api/{vaultName}/state/{documentId}/{folderId}/{transitionId}/references Get all references Gets all references for the specified file and transition. |
| --- | --- |
| Get | api/{vaultName}/state/{documentId}/{folderId}/transitions Gets the transitions available for the specified file. |
| Get | api/{vaultName}/state/{documentId}/transitions?folderId={folderId} Gets the transitions available for the specified file. |
| Get | api/{vaultName}/state/{transitionId} GET: api/{vaultName}/state/{transitionId} Get transition info Gets information about the specified transition. |
| Post | api/{vaultName}/state/{transitionId}/changestate?revoke={revoke} POST: api/{vaultName}/state/{transitionId}/changestate Change state Changes the state of the specified documents. |
| Post | api/{vaultName}/state/{transitionId}/DynamicNotificationUsers POST: api/{vaultName}/state/{transitionId}/DynamicNotificationUsers Get dynamic notification users Gets the users to notify when the specified items undergo the specified transition. |
| Post | api/{vaultName}/state/{transitionId}/HistoryComments POST: api/{vaultName}/state/{transitionId}/HistoryComments Get transition comment history for multiple files Gets the comment histories for specified files that undergo the specified transition. |
| Post | api/{vaultName}/state/transitions POST: api/{vaultName}/state/transitions Get available transitions for multiple files Gets the transitions available for multiple files. |

See Also

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
