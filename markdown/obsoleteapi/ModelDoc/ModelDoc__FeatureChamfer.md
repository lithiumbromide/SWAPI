---
title: "ModelDoc::FeatureChamfer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureChamfer.htm"
---

# ModelDoc::FeatureChamfer

This method is obsolete and has been superseded by [ModelDoc2::FeatureChamfer](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FeatureChamfer.htm).

Description

This method creates a chamfer feature.

Syntax (OLE Automation)

void ModelDoc.FeatureChamfer ( width, angle, flip)

| Input: | (double) width | Width of the chamfer in meters |
| --- | --- | --- |
| Input: | (double) angle | Angle of the chamfer |
| Input: | (BOOL) flip | 0 if angle is to be measured from the right face 1 if angle is to be measured from the left face |

Syntax (COM)

status = ModelDoc->FeatureChamfer ( width, angle, flip )

| Input: | (double) width | Width of the chamfer in meters |
| --- | --- | --- |
| Input: | (double) angle | Angle of the chamfer |
| Input: | (VARIANT_BOOL) flip | 0 if angle is to be measured from the right face 1 if angle is to be measured from the left face |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
