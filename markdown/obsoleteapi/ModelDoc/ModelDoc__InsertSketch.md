---
title: "ModelDoc::InsertSketch"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSketch.htm"
---

# ModelDoc::InsertSketch

This method is now obsolete and has been superseded by [ModelDoc::InsertSketch2](ModelDoc__InsertSketch2.htm).

Description

This method creates or exits a sketch. If a sketch is not currently active, then this method creates a sketch on the selected planar entity (for example, face, plane, and so on). If a sketch is currently active, then calling this method exits you from the sketch.

Syntax (OLE Automation)

void ModelDoc.InsertSketch ()

Syntax (COM)

status = ModelDoc->InsertSketch ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks
