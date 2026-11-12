---
title: "ModelDoc::InsertSplitLineSil"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSplitLineSil.htm"
---

# ModelDoc::InsertSplitLineSil

This method is obsolete and has been superseded by [ModelDoc2::InsertSplitLineSil](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertSplitLineSil.htm).

Description

This method splits a face by creating split lines along the silhouette of the selected faces. The silhouette curves differs based on your orientation. Therefore, this method requires a selection to specify the desired direction.

Syntax (OLE Automation)

void ModelDoc.InsertSplitLineSil ()

Syntax (COM)

status = ModelDoc->InsertSplitLineSil ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

Valid items for selection to specify the direction would be a reference plane, a planar face, an edge, an axis, or two points.

The items selected for direction specification must be selected and marked using SelectByMark or AndSelectByMark with a mark value of 2.

The faces to be spilt must be selected and marked by SelectByMark or AndSelectByMark with a mark value of 1.
