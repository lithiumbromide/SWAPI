---
title: "ModelDoc2::SketchOffset"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchOffset.htm"
---

# ModelDoc2::SketchOffset

This method is now obsolete and has been superseded by [ModelDoc2::SketchOffset2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchOffset2.htm).

Description

This method offsets the selected sketch segments.

Syntax (OLE Automation)

void ModelDoc2.SketchOffset ( offset, chainMode )

| Input: | (double) offset | Offset value; negative value offsets in opposite direction |
| --- | --- | --- |
| Input: | (BOOL) chainMode | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset |

Syntax (COM)

status = ModelDoc2->SketchOffset ( offset, chainMode )

| Input: | (double) offset | Offset value; negative value offset in opposite direction |
| --- | --- | --- |
| Input: | (BOOL) chainMode | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specifying TRUE for chainMode offsets the selected entity and any other entities that belong to the same contour or chain.
