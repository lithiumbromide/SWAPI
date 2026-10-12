---
title: "ModelView::Scale"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelView/ModelView__Scale.htm"
---

# ModelView::Scale

This property is obsolete and has been superseded by [ModelView::Scale2](sldworksAPI.chm::/ModelView/ModelView__Scale2.htm).

Description

This property gets and sets the scale factor for the view.

Syntax (OLE Automation)

scale = ModelView.Scale (VB Get property)

ModelView.Scale = scale (VB Set property)

scale = ModelView.GetScale ( ) (C++ Get property)

ModelView.SetScale ( scale ) (C++ Set property)

| Property: | (double) scale | View scale |
| --- | --- | --- |

Syntax (Com)

status = ModelView->get_Scale ( &scale )

status = ModelView->put_Scale( scale )

| Property: | (double) scale | View scale |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Using data returned from this property along with information from ModelView::Orientation2 and ModelView::Tranlation2 should be multiplied in this order: orientation -> scale -> transform.

To map your coordinates from 3D space to the screen, use ModelView::Xform.
