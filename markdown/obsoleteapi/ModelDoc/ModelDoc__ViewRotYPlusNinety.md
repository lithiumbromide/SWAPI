---
title: "ModelDoc::ViewRotYPlusNinety"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ViewRotYPlusNinety.htm"
---

# ModelDoc::ViewRotYPlusNinety

This method is obsolete and has been superseded by [ModelDoc2::ViewRotYPlusNinety](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ViewRotYPlusNinety.htm).

Description

This method dynamically rotates the view by 90° about Y.

Syntax (OLE Automation)

void ModelDoc.ViewRotYPlusNinety ()

Syntax (COM)

status = ModelDoc->ViewRotYPlusNinety ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

To increase the speed of dynamic view changes with Hidden Edge or Hidden Greyed display, use ModelView::StartDynamics and ModelView::StopDynamics.
