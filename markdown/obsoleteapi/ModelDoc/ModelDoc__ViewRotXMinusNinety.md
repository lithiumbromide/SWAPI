---
title: "ModelDoc::ViewRotXMinusNinety"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ViewRotXMinusNinety.htm"
---

# ModelDoc::ViewRotXMinusNinety

This method is obsolete and has been superseded by [ModelDoc2::ViewRotXMinusNinety](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ViewRotXMinusNinety.htm).

Description

This method dynamically rotates the view by -90° about X.

Syntax (OLE Automation)

void ModelDoc.ViewRotXMinusNinety ()

Syntax (COM)

status = ModelDoc->ViewRotXMinusNinety ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

To increase the speed of dynamic view changes with Hidden Edge or Hidden Greyed display, use ModelView::StartDynamics and ModelView::StopDynamics.
