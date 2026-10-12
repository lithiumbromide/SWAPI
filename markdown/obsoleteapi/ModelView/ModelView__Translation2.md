---
title: "ModelView::Translation2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelView/ModelView__Translation2.htm"
---

# ModelView::Translation2

This method is obsolete and has been superseded by [ModelView::Translation3](sldworksAPI.chm::/ModelView/ModelView__Translation3.htm).

Description

This property gets and sets the view translation vector. These values are in meters and describe the vector from the current screen center to the center of the bounding box, where the bounding box represents the extents of the current model in this orientation.

Syntax (OLE Automation)

translation = ModelView.Translation2 (VB Get property)

ModelView.Translation2 = translation (VB Set property)

translation = ModelView.GetTranslation2 ( ) (C++ Get property)

ModelView.SetTranslation2 ( translation ) (C++ Set property)

| Property: | (VARIANT) translation | VARIANT of type SafeArray containing the desired view panning translation vector in format of 3 doubles. |
| --- | --- | --- |

Syntax (COM)

status = ModelView->get_ITranslation2( translation)

status = ModelView->put_ITranslation2 ( translation )

| Property: | (double*) translation | Pointer to an array of 3 doubles representing the view panning translation vector |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Using data returned from this property with information from ModelView::Orientation2 and ModelView::Scale2 should be multiplied in this order: 0rientation -> scale -> transform.

To map your coordinates from 3D space to the screen, use ModelView::Xform.

To increase the speed of your view changes, use ModelView::StartDynamics and ModelView::StopDynamics.
