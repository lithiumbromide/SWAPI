---
title: "DrawingDoc::EditRebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__EditRebuild.htm"
---

# DrawingDoc::EditRebuild

This method is obsolete and has been superseded by [ModelDoc2::EditRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditRebuild3.htm).

Description

This method rebuilds the drawing.

Syntax (OLE Automation)

void DrawingDoc.EditRebuild ()

Syntax (COM)

status = DrawingDoc->EditRebuild ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

There are certain situations in which SolidWorks blocks this command. For example, if the user is interactively editing the properties of a dimension, SolidWorks blocks this method because calling it invalidates all of the pointers in the document. If DrawingDoc::EditRebuild is not blocked, closing the Dimension-Properties dialog box might cause problems because the dialog box looks for the original dimension pointer.
