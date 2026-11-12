---
title: "ModelDoc::ViewRotateplusz"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ViewRotateplusz.htm"
---

# ModelDoc::ViewRotateplusz

This method is obsolete and has been superseded by [ModelDoc2::ViewRotateplusz](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ViewRotateplusz.htm).

Description

This method rotates the view around z in a positive direction with the current increment.

Syntax (OLE Automation)

void ModelDoc.ViewRotateplusz ()

Syntax (COM)

status = ModelDoc->ViewRotateplusz ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

To increase the speed of dynamic view changes with Hidden Edge or Hidden Greyed display, use ModelView::StartDynamics and ModelView::StopDynamics.
