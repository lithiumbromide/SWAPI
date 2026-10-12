---
title: "ModelDoc::InsertProjectedSketch2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_InsertProjectedSketch2.htm"
---

# ModelDoc::InsertProjectedSketch2

This method is obsolete and has been superseded by [ModelDoc2::InsertProjectedSketch2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertProjectedSketch2.htm).

Description

This method projects a closed set of entities from the selected sketch onto the selected planar object.

Syntax (OLE Automation)

retval = ModelDoc.InsertProjectedSketch2 ( reverse )

| Input: | (long) reverse | Pass 1 to reverse the projected direction |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created Feature object or NULL if the operation fails |

Syntax (COM)

status = ModelDoc->IInsertProjectedSketch2 ( reverse, &retval )

| Input: | (long) reverse | Pass 1 to reverse the projected direction |
| --- | --- | --- |
| Output: | (LPFEATURE) retval | Pointer to the newly created Feature object or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can reverse the direction in which the curve is projected. This is only necessary when the selected face wraps around the plane of the curve. For example, if the sketch that is being projected is surrounded by a cylindrical face, then two possible projections exist. Use the reverse argument to toggle the direction based on the normal vector of the sketch. The default direction is along the sketch normal.
