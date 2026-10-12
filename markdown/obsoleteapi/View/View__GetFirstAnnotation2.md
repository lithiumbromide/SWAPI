---
title: "View::GetFirstAnnotation2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstAnnotation2.htm"
---

# View::GetFirstAnnotation2

This method is obsolete and has been superseded by [View::GetFirstAnnotation3](sldworksAPI.chm::/View/View__GetFirstAnnotation3.htm).

Description

This method gets the first annotation in the view.

Syntax (OLE Automation)

retval = View.GetFirstAnnotation2( )

| Return: | (LPDISPATCH) retval | Dispatch object for the first Annotation object in the view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetFirstAnnotation2( &retval )

| Output: | (LPANNOTATION) retval | Pointer to the first Annotation object in the view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

The difference between this method and the now obsolete View::GetFirstAnnotation is that this method retrieves any display dimension, including suppressed, hidden, or dangling dimensions. The sheet must be visible. See Sheet::SheetFormatVisible.

A dimension becomes suppressed or hidden when you specifically select a dimension and hide it or when you select a feature and say hide all dimensions. If you need to filter out these dimensions, you must use Annotation::Visible to check that status.

If the annotation is on a layer that is not shown, the annotation is still returned.

If annotations are not displayed or any specific types of annotations are not displayed due to the end-user setting some annotation properties, use ModelDoc2::GetUserPreferenceToggle to discover those situations.
