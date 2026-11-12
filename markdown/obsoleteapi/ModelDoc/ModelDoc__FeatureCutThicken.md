---
title: "ModelDoc::FeatureCutThicken"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureCutThicken.htm"
---

# ModelDoc::FeatureCutThicken

This method is obsolete and has been superseded by [ModelDoc::FeatureCutThicken2](ModelDoc__FeatureCutThicken2.htm).

Description

This method thickens the selected reference surface feature and then generates a cut.

Syntax (OLE Automation)

void ModelDoc.FeatureCutThicken ( thickness, direction, faceIndex )

| Input: | (double)thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long)direction | 0 – Thicken side 1 1 – Thicken side2 2 – Thicken both sides |
| Input: | (long) faceIndex | Not used |

Syntax (COM)

status = ModelDoc->FeatureCutThicken ( thickness, direction, faceIndex )

| Input: | (double)thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long)direction | 0 – Thicken side 1 1 – Thicken side2 2 – Thicken both sides |
| Input: | (long) aceIndex | Not used |
| Return: | (HRESULT)status | S_OK if sccessful |

Remarks
