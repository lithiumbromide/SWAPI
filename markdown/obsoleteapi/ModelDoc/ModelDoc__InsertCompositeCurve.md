---
title: "ModelDoc::InsertCompositeCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCompositeCurve.htm"
---

# ModelDoc::InsertCompositeCurve

This method is obsolete and has been superseded by [ModelDoc2::InsertCompositeCurve](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCompositeCurve.htm).

Description

This method inserts a composite curve based on the selections.

Syntax (OLE Automation)

void ModelDoc.InsertCompositeCurve( )

Syntax (COM)

status = ModelDoc->InsertCompositeCurve( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method is the same as interactively creating a composite curve by selecting Insert, Reference Geometry, Composite Curve.

See SolidWorks Help for more information to find out what entities are valid to select.

To use this method, the selections should be made using a SelectByMark method with a mark number of 1.
