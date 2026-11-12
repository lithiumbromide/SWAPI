---
title: "ModelDoc2::GetFirstAnnotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetFirstAnnotation.htm"
---

# ModelDoc2::GetFirstAnnotation

This method is obsolete and has been superseded by [ModelDoc2::GetFirstAnnotation2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetFirstAnnotation2.htm).

Description

This method gets the first annotation in the model.

Syntax (OLE Automation)

retval = ModelDoc2.GetFirstAnnotation( )

| Return: | (LPDISPATCH)retval | Dispatch object for the first Annotation in the model |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetFirstAnnotation( &retval )

| Output: | (LPANNOTATION)retval | Pointer to the first Annotation in the model |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful. |

Remarks

For parts and assemblies, this method returns the first Annotation object in the model. For drawings, access the annotations using the View::GetFirstAnnotation method.
