---
title: "ModelDoc::AutoSolveToggle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AutoSolveToggle.htm"
---

# ModelDoc::AutoSolveToggle

This method is obsolete and has been superseded by [ModelDoc2::AutoSolveToggle](../ModelDoc2/ModelDoc2__AutoSolveToggle.htm).

Description

This method specifies whether SolidWorks should solve the sketch geometry as you create the sketch.

Syntax (OLE Automation)

void ModelDoc.AutoSolveToggle ()

Syntax (COM)

status = ModelDoc->AutoSolveToggle ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

If this method is turned on, then computations are solved automatically. When you are in the process of changing many dimensions in an active sketch, you may want to turn off the automatic-solve capability temporarily.
