---
title: "ModelDoc2::FeatureBossThicken"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureBossThicken.htm"
---

# ModelDoc2::FeatureBossThicken

This method is obsolete and has been superseded by [FeatureBossThicken2](ModelDoc2__FeatureBossThicken2.htm).

Description

This method creates a boss feature by thickening the selected reference surface.

Syntax (OLE Automation)

void ModelDoc2.FeatureBossThicken ( thickness, direction, faceIndex )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 - Thicken side 1 1 - Thicken side2 2 - Thicken both side |
| Input: | (long) NotUsed | Not used |

Syntax (COM)

status = ModelDoc2->FeatureBossThicken ( thickness, direction, faceIndex )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 - Thicken side 1 1 - Thicken side2 2 - Thicken both side |
| Input: | (long) NotUsed | Not used |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a boss feature by thickening the selected reference surface.
