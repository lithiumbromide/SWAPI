---
title: "ModelDoc::InsertSheetMetalMiterFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSheetMetalMiterFlange.htm"
---

# ModelDoc::InsertSheetMetalMiterFlange

This method is obsolete and has been superseded by [ModelDoc2::InsertSheetMetalMiterFlange](../ModelDoc2/ModelDoc2__InsertSheetMetalMiterFlange.htm).

Description

This method inserts a sheet metal miter flange into this model document.

Syntax (OLE Automation)

void ModelDoc.InsertSheetMetalMiterFlange ( useReliefRatio, useDefaultGap, useAutoRelief, globalRadius, ripGap, autoReliefRatio, autoReliefWidth, autoReliefDepth, reliefType, ripLocation)

| Input: | (BOOL) useReliefRatio | TRUE to use the relief ratio value, FALSE otherwise |
| --- | --- | --- |
| Input: | (BOOL) useDefaultGap | TRUE to use the default gap value, FALSE otherwise |
| Input: | (BOOL) useAutoRelief | TRUE to use auto relief, FALSE otherwise |
| Input: | (double) globalRadius | Value for the global radius |
| Input: | (double) ripGap | Value for the rip-gap |
| Input: | (double) autoReliefRatio | Value for the auto-relief ratio |
| Input: | (double) autoReliefWidth | Value for the auto-relief width |
| Input: | (double) autoReliefDepth | Value for the auto-relief depth |
| Input: | (long) reliefType | Relief type specifier; currently only supports 0 – Tear relief type |
| Input: | (long) ripLocation | Value for the rip location: 0 = Start 1 = End 2 = Start and End |

Syntax (COM)

status = ModelDoc->InsertSheetMetalMiterFlange ( useReliefRatio, useDefaultGap, useAutoRelief, globalRadius, ripGap, autoReliefRatio, autoReliefWidth, autoReliefDepth, reliefType, ripLocation)

| Input: | (VARIANT_BOOL) useReliefRatio | TRUE to use the relief ratio value, FALSE otherwise |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) useDefaultGap | TRUE to use the default gap value, FALSE otherwise |
| Input: | (VARIANT_BOOL) useAutoRelief | TRUE to use auto relief, FALSE otherwise |
| Input: | (double) globalRadius | Value for the global radius |
| Input: | (double) ripGap | Value for the rip-gap |
| Input: | (double) autoReliefRatio | Value for the auto relief ratio |
| Input: | (double) autoReliefWidth | Value for the auto relief width |
| Input: | (double) autoReliefDepth | Value for the auto relief depth |
| Input: | (long) reliefType | relief type specifier: currently only supports 0 – Tear relief type |
| Input: | (long) ripLocation | Value for the rip location: 0 = Start 1 = End 2 = Start and End |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
