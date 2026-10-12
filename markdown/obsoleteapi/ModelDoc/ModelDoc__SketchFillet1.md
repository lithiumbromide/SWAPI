---
title: "ModelDoc::SketchFillet1"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchFillet1.htm"
---

# ModelDoc::SketchFillet1

This method is obsolete and has been superseded by [ModelDoc::SketchFillet2](ModelDoc__SketchFillet2.htm).

Description

This method creates a fillet between the two selected sketch entities.

Syntax (OLE Automation)

(void) ModelDoc.SketchFillet1 ( rad )

| Input: | (double) rad | Radius for the fillet |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SketchFillet1 ( rad )

| Input: | (double)rad | Radius for the fillet |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If one of the sketch entities is constrained (for example, the length is dimensioned), then this method maintains the original corner geometry. If neither of the sketch entities are dimensioned, then the geometry is removed in the fillet operation.
