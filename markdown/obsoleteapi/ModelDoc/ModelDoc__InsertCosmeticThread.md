---
title: "ModelDoc::InsertCosmeticThread"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCosmeticThread.htm"
---

# ModelDoc::InsertCosmeticThread

This method is obsolete and has been superseded by [ModelDoc2::InsertCosmeticThread](../ModelDoc2/ModelDoc2__InsertCosmeticThread.htm).

Description

This method inserts a cosmetic-thread annotation based on the selected edge.

Syntax (OLE Automation)

void ModelDoc.InsertCosmeticThread ( type, dia, length, note)

| Input: | (short) type | Thread type where Blind = 0 and UpToNext = 1 |
| --- | --- | --- |
| Input: | (double) dia | Major diameter |
| Input: | (double) length | Thread depth (length) |
| Input: | (BSTR) note | Callout string to display in the drawing document |

Syntax (COM)

status = ModelDoc->InsertCosmeticThread ( type, dia, length, note )

| Input: | (short) type | Thread type where Blind = 0 and UpToNext = 1 |
| --- | --- | --- |
| Input: | (double) dia | Mmajor diameter |
| Input: | (double) length | Thread depth (length) |
| Input: | (BSTR) note | Callout string to display in the drawing document |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
