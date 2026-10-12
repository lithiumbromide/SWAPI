---
title: "ModelDoc2::InsertSheetMetal3dBend"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSheetMetal3dBend.htm"
---

# ModelDoc2::InsertSheetMetal3dBend

This method is obsolete and has been superseded by [FeatureManager::InsertSheetMetal3dBend](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertSheetMetal3dBend.htm).

Description

This method inserts a 3D bend in the sheet metal part in the model document.

Syntax (OLE Automation)

void ModelDoc2.InsertSheetMetal3dBend ( angle, radius, flipDir, bendPos)

| Input: | (double) angle | Angle of the bend that you are inserting |
| --- | --- | --- |
| Input: | (double) radius | Radius of the bend you are inserting |
| Input: | (BOOL) flipDir | TRUE to flip the bend direction, FALSE otherwise |
| Input: | (short) bendPos | Value of the bend position |

Syntax (COM)

status = ModelDoc2->InsertSheetMetal3dBend ( angle, radius, flipDir, bendPos )

| Input: | (double) angle | Angle of the bend that you are inserting |
| --- | --- | --- |
| Input: | (double) radius | Radius of the bend you are inserting |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the bend direction, FALSE otherwise |
| Input: | (short) bendPos | Value of the bend position |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Value of the bend positions are:

- 0 = bend centerline
- 1 = material inside
- 2 = material outside
- 3 = bend outside
