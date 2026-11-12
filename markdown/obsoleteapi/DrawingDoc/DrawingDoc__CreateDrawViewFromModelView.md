---
title: "DrawingDoc::CreateDrawViewFromModelView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateDrawViewFromModelView.htm"
---

# DrawingDoc::CreateDrawViewFromModelView

This method is obsolete and has been superseded by [DrawingDoc::CreateDrawViewFromModelView2](DrawingDoc__CreateDrawViewFromModelView2.htm).

Description

This method creates a drawing view on the current drawing sheet using the specified model view.

Syntax (OLE Automation)

retval = DrawingDoc.CreateDrawViewFromModelView ( modelName, viewName, locX, locY, locZ)

| Input: | (BSTR) modelName | Name of the document to create the view from (including the .sldprt or .sldasm extension) |
| --- | --- | --- |
| Input: | (BSTR) viewName | Name of the model view to create the view from (see Remarks ) |
| Input: | (double) locX | X-location of drawing view center in meters |
| Input: | (double) locY | Y-location of drawing view center in meters |
| Input: | (double) locZ | Z-location of drawing view center in meters |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateDrawViewFromModelView ( modelName, viewName, locX, locY, locZ, &retval )

| Input: | (BSTR) modelName | Name of the document to create the view from (including the .sldprt or .sldasm extension) |
| --- | --- | --- |
| Input: | (BSTR) viewName | Name of the model view to create the view from (see Remarks ) |
| Input: | (double) locX | X-location of drawing view center in meters |
| Input: | (double) locY | Y-location of drawing view center in meters |
| Input: | (double) locZ | Z-location of drawing view center in meters |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method places the center of the view at the specified location.

The modelName must be an open document in the current SolidWorks session. The viewName must exactly match the name of the model view. For example, the names of the standard views begin with an asterisk. This asterisk is part of the view name and must be included (for example, "*Front").
