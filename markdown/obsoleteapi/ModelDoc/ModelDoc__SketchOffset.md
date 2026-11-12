---
title: "ModelDoc::SketchOffset"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchOffset.htm"
---

# ModelDoc::SketchOffset

This method is obsolete and has been superseded by [ModelDoc::SketchOffset2](ModelDoc__SketchOffset2.htm).

Description

This method offsets the selected sketch segments.

Syntax (OLE Automation)

void ModelDoc.SketchOffset ( offset, chainMode )

| Input: | (double) offset | Offset value; negative value will offset in opposite direction |
| --- | --- | --- |
| Input: | (BOOL) chainMode | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset |

Syntax (COM)

status = ModelDoc->SketchOffset ( offset, chainMode )

| Input: | (double) offset | Offset value; negative value will offset in opposite direction |
| --- | --- | --- |
| Input: | (BOOL) chainMode | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specifying TRUE to the chainMode argument offsets the selected entity and any other entities that belong to the same contour or chain.
