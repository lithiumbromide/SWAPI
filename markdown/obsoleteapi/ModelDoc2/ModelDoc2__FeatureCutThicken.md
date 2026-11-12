---
title: "ModelDoc2::FeatureCutThicken"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureCutThicken.htm"
---

# ModelDoc2::FeatureCutThicken

This method is obsolete and has been superseded by [ModelDoc2::FeatureCutThicken2](ModelDoc2__FeatureCutThicken2.htm).

Description

This method creates a cut feature by thickening the selected reference surface.

Syntax (OLE Automation)

void ModelDoc2.FeatureCutThicken ( thickness, direction, faceIndex )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 - Thicken side 1 1 - Thicken side2 2 - Thicken both sides |
| Input: | (long) faceIndex | Not used |

Syntax (COM)

status = ModelDoc2->FeatureCutThicken ( thickness, direction, faceIndex )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 - Thicken side 1 1 - Thicken side2 2 - Thicken both sides |
| Input: | (long) faceIndex | Not used |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
