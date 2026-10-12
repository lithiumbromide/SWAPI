---
title: "ModelDoc::InsertConnectionPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertConnectionPoint.htm"
---

# ModelDoc::InsertConnectionPoint

This method is obsolete and has been superseded by [ModelDoc2::InsertConnectionPoint](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertConnectionPoint.htm).

Description

This method adds a connection point based on the selected point and selected planar item. If the selection set is not complete, then the Insert Connection Point dialog is displayed.

Syntax (OLE Automation)

void ModelDoc.InsertConnectionPoint ( )

Syntax (COM)

status = ModelDoc->InsertConnectionPoint ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

The connection point is the point on the fitting that defines where the connection to other pipe items begin or end.
