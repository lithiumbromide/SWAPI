---
title: "ModelDoc::ChangeSketchPlane"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ChangeSketchPlane.htm"
---

# ModelDoc::ChangeSketchPlane

This method is obsolete and has been superseded by [ModelDoc2::ChangeSketchPlane](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ChangeSketchPlane.htm).

Description

Every sketch is associated with a plane (that is, a reference plane or a planar face). This method changes the plane used by a sketch by moving the selected sketch to a selected plane.

Syntax (OLE Automation)

retval = ModelDoc.ChangeSketchPlane ()

| Return: | (BOOL) retval | TRUE if the change was successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->ChangeSketchPlane ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the change was successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires that the sketch and the new plane or face are selected when it is called.
