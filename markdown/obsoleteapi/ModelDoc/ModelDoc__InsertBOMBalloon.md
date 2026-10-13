---
title: "ModelDoc::InsertBOMBalloon"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertBOMBalloon.htm"
---

# ModelDoc::InsertBOMBalloon

This method is obsolete and has been superseded by [ModelDoc::InsertBOMBalloon2](ModelDoc__InsertBOMBalloon2.htm)

Description

This method inserts a BOM balloon based on the selected object. The selected object can be an edge, silhouette, face, or vertex.

Syntax (OLE Automation)

(void) ModelDoc.InsertBOMBalloon ( )

Syntax (COM)

status = ModelDoc->InsertBOMBalloon ( )

| Return: | (HRESULT)status | S_OK if successful |
| --- | --- | --- |

Remarks

The generated BOM balloon uses the current settings for:

- Balloon Style
- Balloon Fit
- BOM balloon upper and lower text (item number, quantity, custom)
