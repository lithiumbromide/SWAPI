---
title: "ModelDoc::ViewRotateminusx"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ViewRotateminusx.htm"
---

# ModelDoc::ViewRotateminusx

This method is obsolete and has been superseded by [ModelDoc2::ViewRotateminusx](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ViewRotateminusx.htm).

Description

This function dynamically rotates the view around x in a negative direction with the current increment.

Syntax (OLE Automation)

void ModelDoc.ViewRotateminusx ()

Syntax (COM)

status = ModelDoc->ViewRotateminusx ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

To increase the speed of dynamic view changes with Hidden Edge or Hidden Greyed display, use ModelView::StartDynamics and ModelView::StopDynamics.
