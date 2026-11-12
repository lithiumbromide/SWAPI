---
title: "ModelDoc::ViewRotateplusy"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ViewRotateplusy.htm"
---

# ModelDoc::ViewRotateplusy

This method is obsolete and has been superseded by [ModelDoc2::ViewRotateplusy](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ViewRotateplusy.htm).

Description

This method rotates the view around y in a positive direction with the current increment.

Syntax (OLE Automation)

void ModelDoc.ViewRotateplusy ()

Syntax (COM)

status = ModelDoc->ViewRotateplusy ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

To increase the speed of dynamic view changes with Hidden Edge or Hidden Greyed display, use ModelView::StartDynamics and ModelView::StopDynamics.
