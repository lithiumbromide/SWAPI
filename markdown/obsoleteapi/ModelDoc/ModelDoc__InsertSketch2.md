---
title: "ModelDoc::InsertSketch2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSketch2.htm"
---

# ModelDoc::InsertSketch2

This method is obsolete and has been superseded by [ModelDoc2::InsertSketch2](../ModelDoc2/ModelDoc2__InsertSketch2.htm).

Description

This method creates or exits a sketch. If a sketch is not currently active, then this method will create a sketch on the selected planar entity (for example, face, plane, and so on). If a sketch is currently active, then calling this method will exit you from the sketch.

Syntax (OLE Automation)

void ModelDoc.InsertSketch2 ( updateEditRebuild )

| Input: | (VARIANT_BOOL) updateEditRebuild | TRUE to update the model, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->InsertSketch2 ( updateEditRebuild )

| Input: | (VARIANT_BOOL) updateEditRebuild | TRUE to update the model, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
