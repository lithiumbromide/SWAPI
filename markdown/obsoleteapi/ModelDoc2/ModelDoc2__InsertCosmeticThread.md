---
title: "ModelDoc2::InsertCosmeticThread"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCosmeticThread.htm"
---

# ModelDoc2::InsertCosmeticThread

This method is obsolete and has been superseded by [FeatureManager::InsertCosmeticThread](../FeatureManager/FeatureManager__InsertCosmeticThread.htm).

Description

This method insert a cosmetic thread annotation based on the selected edge.

Syntax (OLE Automation)

void ModelDoc2.InsertCosmeticThread ( type, dia, length, note)

| Input: | (short) type | Thread type: Blind = 0 UpToNext = 1 |
| --- | --- | --- |
| Input: | (double) dia | The major diameter |
| Input: | (double) length | The thread depth (length) |
| Input: | (BSTR) note | Callout text to display in the drawing document |

Syntax (COM)

status = ModelDoc2->InsertCosmeticThread ( type, dia, length, note )

| Input: | (short) type | Thread type: Blind = 0 UpToNext = 1 |
| --- | --- | --- |
| Input: | (double) dia | The major diameter |
| Input: | (double) length | The thread depth (length) |
| Input: | (BSTR) note | Callout text to display in the drawing document |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
