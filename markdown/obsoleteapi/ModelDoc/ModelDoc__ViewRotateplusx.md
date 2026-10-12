---
title: "ModelDoc::ViewRotateplusx"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ViewRotateplusx.htm"
---

# ModelDoc::ViewRotateplusx

This method is obsolete and has been superseded by [ModelDoc2::ViewRotateplusx](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ViewRotateplusx.htm).

Description

This method rotates the view around x in a positive direction with the current increment.

Syntax (OLE Automation)

void ModelDoc.ViewRotateplusx ()

Syntax (COM)

status = ModelDoc->ViewRotateplusx ( )

| Return: | (HRESULT status | S_OK if successful |
| --- | --- | --- |

Remarks

To increase the speed of dynamic view changes with Hidden Edge or Hidden Greyed display, use ModelView::StartDynamics and ModelView::StopDynamics.
