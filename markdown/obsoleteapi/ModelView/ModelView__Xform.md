---
title: "ModelView::Xform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelView/ModelView__Xform.htm"
---

# ModelView::Xform

This method is obsolete and has been superseded by [ModelView::Transform](sldworksAPI.chm::/ModelView/ModelView__Transform.htm).

Description

This property gets the total transform to go from 3D space to the screen.

Syntax (OLE Automation)

Xform = ModelView.Xform (VB Get property)

Xform = ModelView.GetXform ( ) (C++ Get property)

| Property: | (VARIANT) Xform | VARIANT of type SafeArray of 16 doubles; first 9 are elements of 3x3 rotation matrix, next 3 define translation, next element is scaling, and the last 3 elements are not used |
| --- | --- | --- |

Syntax (Com)

status = ModelView->get_IXform( Xform)

| Property: | (double*) Xform | Pointer to an array of 16 doubles; first 9 are elements of 3x3 rotation matrix, next 3 define translation, next element is scaling, and the last 3 elements are not used |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is typically used when you are grabbing the view handle using ModelView::GetViewHWnd and drawing to the view. For example, if you had a point located at 2,2,2 in model space coordinates, then you could multiply it by this return value to determine where to draw in screen space coordinates. The result will be pixel values for the current view.

The screen space coordinate system has its origin in the upper-left corner of the current view with the X vector pointing to the right and the Y vector pointing down.

If the SolidWorks file is in view-only mode and is not displaying a shaded image, then you cannot perform any view rotations. In this situation, you should not call any of the view rotation APIs.

To determine if the file is in view-only mode and whether it is shaded or not, see ModelDoc2::IsOpenedViewOnly and ModelView::GetDisplayState.
