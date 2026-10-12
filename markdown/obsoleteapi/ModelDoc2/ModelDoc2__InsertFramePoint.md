---
title: "ModelDoc2::InsertFramePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertFramePoint.htm"
---

# ModelDoc2::InsertFramePoint

This method is obsolete and was not superseded.

Description

This method inserts a frame point into the active sketch for the selected spline at the given coordinates.

Syntax (OLE Automation)

void ModelDoc2.InsertFramePoint ( x, y, z )

| Input: | (double) x | x coordinate of frame point |
| --- | --- | --- |
| Input: | (double) y | y coordinate of frame point |
| Input: | (double) z | z coordinate of frame point |

Syntax (COM)

status = ModelDoc2->InsertFramePoint ( x, y, z )

| Input: | (double) x | x coordinate of frame point |
| --- | --- | --- |
| Input: | (double) y | y coordinate of frame point |
| Input: | (double) z | z coordinate of frame point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
