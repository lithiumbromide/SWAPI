---
title: "DrawingDoc::ForceRebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__ForceRebuild.htm"
---

# DrawingDoc::ForceRebuild

This method is obsolete and has been superseded by [ModelDoc2::ForceRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ForceRebuild3.htm).

Description

This method forces a rebuild of the drawing.

Syntax (OLE Automation)

void DrawingDoc.ForceRebuild ( )

Syntax (COM)

status = DrawingDoc->ForceRebuild ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method is equivalent to interactively pressing the Ctrl and Q keys.

This method rebuilds the entire model whether or not it needs to be rebuilt, which can be very time consuming.
