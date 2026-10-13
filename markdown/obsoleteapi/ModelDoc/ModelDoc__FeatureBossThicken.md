---
title: "ModelDoc::FeatureBossThicken"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureBossThicken.htm"
---

# ModelDoc::FeatureBossThicken

This method is obsolete and has been superseded by [ModelDoc::FeatureBossThicken2](ModelDoc__FeatureBossThicken2.htm).

Description

This method creates a thicken feature and then a boss .

Syntax (OLE Automation)

void ModelDoc.FeatureBossThicken ( thickness, direction, faceIndex )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 – Thicken side 1 1 – Thicken side2 2 – Thicken both sides |
| Input: | (long) NotUsed | Not used |

Syntax (COM)

status = ModelDoc->FeatureBossThicken ( thickness, direction, faceIndex )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 – Thicken side 1 1 – Thicken side2 2 – Thicken both sides |
| Input: | (long) NotUsed | Not used |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a boss feature by thickening the selected reference surface.
