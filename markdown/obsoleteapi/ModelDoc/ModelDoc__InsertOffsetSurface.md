---
title: "ModelDoc::InsertOffsetSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertOffsetSurface.htm"
---

# ModelDoc::InsertOffsetSurface

This method is obsolete and has been superseded by [ModelDoc2::InsertOffsetSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertOffsetSurface.htm).

Description

This method inserts an offset surface.

Syntax (OLE Automation)

void ModelDoc.InsertOffsetSurface ( thickness, reverse )

| Input: | (double) offset | Offset of surface from reference |
| --- | --- | --- |
| Input: | (BOOL) reverse | TRUE to reverse the direction of the offset, FALSE to not |

Syntax (COM)

status = ModelDoc->InsertOffsetSurface ( thickness, reverse )

| Input: | (double) offset | Offset of surface from reference |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverse | TRUE to reverse the direction of the offset |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as interactively creating a planar surface by selecting Insert, Reference Geometry, Offset Surface. See the SolidWorks Help for more information about what entities are valid for selection.

Make the selections using ModelDoc::SelectByID before calling this method.
