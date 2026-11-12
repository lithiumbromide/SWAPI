---
title: "ModelDoc::InsertSewRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSewRefSurface.htm"
---

# ModelDoc::InsertSewRefSurface

This method is obsolete and has been superseded by [ModelDoc2::InsertSewRefSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertSewRefSurface.htm).

Description

This method creates a surface by knitting surfaces together.

Syntax (OLE Automation)

void ModelDoc.InsertSewRefSurface( )

Syntax (COM)

status = ModelDoc->InsertSewRefSurface( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method is the same as interactively creating a knit surface by selecting Insert, Reference Geometry, Knit Surface. See SolidWorks Help for more information about what entities are valid for selection.

Make the selections using SelectByMark with a mark of 1.
