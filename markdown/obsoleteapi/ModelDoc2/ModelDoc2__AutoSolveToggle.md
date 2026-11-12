---
title: "ModelDoc2::AutoSolveToggle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AutoSolveToggle.htm"
---

# ModelDoc2::AutoSolveToggle

This method is obsolete and has been superseded by [SketchManager::AutoSolve](sldworksAPI.chm::/SketchManager/SketchManager__AutoSolve.htm).

Description

This method specifies whether or not SolidWorks should automatically solve the sketch geometry of your part while you create it.

Syntax (OLE Automation)

void ModelDoc2.AutoSolveToggle ()

Syntax (COM)

status = ModelDoc2->AutoSolveToggle ( )

| Return: | (HRESULT)status | S_OK if successful |
| --- | --- | --- |

Remarks

If this method is set on, then computations are solved automatically. When you are in the process of changing many dimensions in an active sketch, you may want to temporarily turn off automatic solving.
