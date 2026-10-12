---
title: "ModelDoc2::SketchFillet1"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchFillet1.htm"
---

# ModelDoc2::SketchFillet1

This method is obsolete and has been superseded by [ModelDoc2::SketchFillet2](ModelDoc2__SketchFillet2.htm).

Description

This method creates a fillet between the two selected sketch entities.

Syntax (OLE Automation)

(void) ModelDoc2.SketchFillet1 ( rad )

| Input: | (double) rad | Radius for the fillet |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->SketchFillet1 ( rad )

| Input: | (double) rad | Radius for the fillet |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| If... | Then... |
| --- | --- |
| One of the sketch entities is constrained (for example, the length is dimensioned | Original corner geometry maintained. |
| Neither of the sketch entities are dimensioned | Geometry is removed in the fillet operation. |
