---
title: "ModelDoc::GetActiveSketch2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetActiveSketch2.htm"
---

# ModelDoc::GetActiveSketch2

This method is obsolete and has been superseded by [ModelDoc2::GetActiveSketch2](../ModelDoc2/ModelDoc2__GetActiveSketch2.htm).

Description

This function returns the Sketch object for the currently active 2D or 3D.

Syntax (OLE Automation)

retval = ModelDoc.GetActiveSketch2 ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a sketch. |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetActiveSketch2 ( &retval )

| Output: | (LPSKETCH) retval | Pointer to a Sketch object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before you can use this method, you must select and activate a sketch. You can use ModelDoc::SelectByID to select a sketch, and ModelDoc::InsertSketch2 to make the sketch active.
