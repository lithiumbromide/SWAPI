---
title: "ModelDoc::InsertSheetMetal3dBend"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSheetMetal3dBend.htm"
---

# ModelDoc::InsertSheetMetal3dBend

This method is obsolete and has been superseded by [ModelDoc2::InsertSheetMetal3dBend](../ModelDoc2/ModelDoc2__InsertSheetMetal3dBend.htm).

Description

This method inserts a sheet metal 3D bend.

Syntax (OLE Automation)

void ModelDoc.InsertSheetMetal3dBend ( angle, radius, flipDir, bendPos)

| Input: | (double) angle | Angle of the bend that you are inserting |
| --- | --- | --- |
| Input: | (double) radius | Radius of the bend you are inserting |
| Input: | (BOOL) flipDir | TRUE to flip the bend direction, FALSE otherwise |
| Input: | (short) bendPos | Value of the bend position |

Syntax (COM)

status = ModelDoc->InsertSheetMetal3dBend ( angle, radius, flipDir, bendPos )

| Input: | (double) angle | Angle of the bend that you are inserting. |
| --- | --- | --- |
| Input: | (double) radius | Radius of the bend you are inserting |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the bend direction, FALSE otherwise |
| Input: | (short) bendPos | Value of the bend position |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The value of the bend positions are:

- 0 = Bend centerline
- 1 = Material inside
- 2 = Material outside
- 3 = Bend 0utside
