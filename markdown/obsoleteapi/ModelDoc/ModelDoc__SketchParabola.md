---
title: "ModelDoc::SketchParabola"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchParabola.htm"
---

# ModelDoc::SketchParabola

This method is obsolete and has been superseded by [ModelDoc2::SketchParabola](../ModelDoc2/ModelDoc2__SketchParabola.htm).

Description

This method inserts a parabola in the active sketch.

Syntax (OLE Automation)

void ModelDoc.SketchParabola( FocusX, FocusY, FocusZ, ApexX, ApexY, ApexZ, StartX, StartY, StartZ, EndX, EndY, EndZ )

| Input: | (double) FocusX, FocusY, FocusZ | Location of the focus of the parabola |
| --- | --- | --- |
| Input: | (double) ApexX, ApexY, ApexZ | Location of the apex of the parabola |
| Input: | (double) StartX, StartY, StartZ | Location of the start of the parabola |
| Input: | (double) EndX, EndY, EndZ | Location of the end of the parabola |

Syntax (COM)

status = ModelDoc->SketchParabola( FocusX, FocusY, FocusZ, ApexX, ApexY, ApexZ, StartX, StartY, StartZ, EndX, EndY, EndZ )

| Input: | (double) FocusX, FocusY, FocusZ | Location of the focus of the parabola |
| --- | --- | --- |
| Input: | (double) ApexX, ApexY, ApexZ | Location of the apex of the parabola |
| Input: | (double) StartX, StartY, StartZ | Location of the start of the parabola |
| Input: | (double) EndX, EndY, EndZ | Location of the end of the parabola |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
