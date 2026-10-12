---
title: "DrawingDoc::CreateDrawViewFromModelView2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateDrawViewFromModelView2.htm"
---

# DrawingDoc::CreateDrawViewFromModelView2

This method is obsolete and has been superseded by [DrawingDoc::CreateDrawViewFromModelView3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateDrawViewFromModelView3.htm).

Description

This method creates a drawing view on the current drawing sheet using the specified model view.

Syntax (OLE Automation)

retval = DrawingDoc.CreateDrawViewFromModelView2 ( modelName, viewName, locX, locY, locZ)

| Input: | (BSTR) modelName | Name of the document from which to create the view (including the .sldprt or .sldasm filename extension) |
| --- | --- | --- |
| Input: | (BSTR) viewName | Name of the model view from which to create the view (see Remarks ) |
| Input: | (double) locX | x location of drawing view center in meters |
| Input: | (double) locY | y location of drawing view center in meters |
| Input: | (double) locZ | z location of drawing view center in meters |
| Output: | (LPVIEW) retval | Pointer to the newly create View object |

Syntax (COM)

status = DrawingDoc->CreateDrawViewFromModelView2 ( modelName, viewName, locX, locY, locZ, &retval)

| Input: | (BSTR) modelName | Name of the document from which to create the view (including the .sldprt or .sldasm filename extension) |
| --- | --- | --- |
| Input: | (BSTR) viewName | Name of the model view from which to create the view (see Remarks ) |
| Input: | (double) locX | x location of drawing view center in meters |
| Input: | (double) locY | y location of drawing view center in meters |
| Input: | (double) locZ | z location of drawing view center in meters |
| Output: | (LPVIEW) retval | Pointer to the newly create View object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method places the center of the view at the specified location.

The modelName must be an open document in the current SolidWorks session. The viewName must exactly match the name of the model view. For example, the names of the standard views begin with an asterisk. This asterisk is part of the view name and must be included (for example, "*Front").
