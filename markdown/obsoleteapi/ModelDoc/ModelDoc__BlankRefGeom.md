---
title: "ModelDoc::BlankRefGeom"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__BlankRefGeom.htm"
---

# ModelDoc::BlankRefGeom

This method is obsolete and has been superseded by [ModelDoc2::BlankRefGeom](sldworksAPI.chm::/ModelDoc2/ModelDoc2__BlankRefGeom.htm).

Description

This method hides the selected reference geometry in the graphics window.

Syntax (OLE Automation)

void ModelDoc.BlankRefGeom ()

Syntax (COM)

status = ModelDoc->BlankRefGeom ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

If you select a reference plane and call this function, the plane will be invisible in the graphics area. This method has the same effect as selecting an item and choosing Hide from the shortcut menu.
