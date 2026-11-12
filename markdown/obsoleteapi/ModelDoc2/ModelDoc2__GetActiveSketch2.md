---
title: "ModelDoc2::GetActiveSketch2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetActiveSketch2.htm"
---

# ModelDoc2::GetActiveSketch2

This method is obsolete and has been superseded by [SketchManager::ActiveSketch.](sldworksAPI.chm::/SketchManager/SketchManager__ActiveSketch.htm)

Description

This method returns the active sketch.

Syntax (OLE Automation)

retval = ModelDoc2.GetActiveSketch2 ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a sketch |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetActiveSketch2 ( &retval )

| Output: | (LPSKETCH) retval | Pointer to the Sketch object for the active sketch |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Before you can use this method, you must select and activate a sketch. You can use ModelDocExtension::SelectByID2 to select a sketch and SketchManager::InsertSketch to make the sketch active.

For an example of getting a sketch through feature traversal, see Get Sketches Example.
