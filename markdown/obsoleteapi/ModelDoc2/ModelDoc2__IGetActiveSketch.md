---
title: "ModelDoc2::GetActiveSketch"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__IGetActiveSketch.htm"
---

# ModelDoc2::GetActiveSketch

This method is obsolete and has been superseded by [ModelDoc2::](ModelDoc2__GetActiveSketch2.htm)GetActiveSketch2.

Description

This method returns the active sketch in document. If a sketch is not currently active, or if the active sketch is a 3D sketch, then NULL is returned.

Syntax (OLE Automation)

retval = ModelDoc2.GetActiveSketch ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a sketch |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetActiveSketch ( &retval )

| Output: | (LPSKETCH) retval | Pointer to the active Sketch object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before you can use this method, you must select and activate a sketch. You can use ModelDoc2::SelectByID to select a sketch and ModelDoc2::InsertSketch2 to make the sketch active.

To avoid regressions in existing applications, this method returns NULL if the active sketch is a 3D sketch. To access the active 2D or 3D sketch, use ModelDoc2::GetActiveSketch2. To determine if a Sketch object is 2D or 3D, use Sketch::Is3D.

For an example of getting a sketch through Feature traversal, see Get Sketches Example.
