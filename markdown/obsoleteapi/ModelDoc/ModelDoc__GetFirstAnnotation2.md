---
title: "ModelDoc::GetFirstAnnotation2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetFirstAnnotation2.htm"
---

# ModelDoc::GetFirstAnnotation2

This method is obsolete and has been superseded by [ModelDoc2::GetFirstAnnotation2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetFirstAnnotation2.htm).

Description

This method gets the first annotation in the model.

Syntax (OLE Automation)

retval = ModelDoc.GetFirstAnnotation2( )

| Return: | (LPDISPATCH) retval | Dispatch object for the first Annotation object in the model |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetFirstAnnotation2( &retval )

| Output: | (LPANNOTATION) retval | Pointer to the first Annotation object in the model |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For part and assembly documents, this method returns the first Annotation object in the model. For drawing documents, access annotations using View::GetFirstAnnotation2.

The difference between ModelDoc::GetFirstAnnotation and ModelDoc::GetFirstAnnotation2 is that ModelDoc::GetFirstAnnotation2 retrieves any display dimension, including suppressed, hidden, or dangling dimensions.

A dimension becomes suppressed or hidden when you specifically select a dimension and hide it, or when you select a feature and say hide all dimensions. So if you need to filter out these dimensions, you will have to use the Annotation::Visible API to check that status.

If the annotation is on a layer that isn't shown, the annotation will still be returned.

If annotations are not displayed, or any specific types of annotations are not displayed due to user Annotation Properties settings, the [ModelDoc::GetUserPreferenceToggle](ModelDoc__GetUserPreferenceToggle.htm) API can be used to discover those situations.
