---
title: "ModelDoc::GetActiveSketch"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetActiveSketch.htm"
---

# ModelDoc::GetActiveSketch

This method is obsolete and has been superseded by [ModelDoc::GetActiveSketch2](ModelDoc__GetActiveSketch2.htm).

Description

This method returns the active sketch in document. If no sketch is currently active, or if the active sketch is a 3D sketch, then NULL is returned.

Syntax (OLE Automation)

retval = ModelDoc.GetActiveSketch ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a sketch |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetActiveSketch ( &retval )

| Output: | (LPSKETCH) retval | Pointer to a Sketch object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before you can use this method, you must select and activate a sketch. You can use ModelDoc::SelectByID to select a sketch and ModelDoc::InsertSketch2 to make the sketch active.

To avoid regressions in existing applications, this method returns NULL if the active sketch is a 3D sketch. To access the active 2D or 3D sketch, see GetActiveSketch2. To determine if a Sketch object is 2D or 3D, use Sketch::Is3D.
