---
title: "ModelDoc::GetFirstAnnotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetFirstAnnotation.htm"
---

# ModelDoc::GetFirstAnnotation

This method is obsolete and has been superseded by [ModelDoc::GetFirstAnnotation2](ModelDoc__GetFirstAnnotation2.htm).

Description

This method gets the first annotation in the model.

Syntax (OLE Automation)

retval = ModelDoc.GetFirstAnnotation( )

| Return: | (LPDISPATCH) retval | Dispatch object for the first Annotation object in the model |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetFirstAnnotation( &retval )

| Output: | (LPANNOTATION) retval | Pointer to the first Annotation object in the model |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For part and assembly documents, this method returns the first Annotation object in the model. For drawing documents, access the annotations using View::GetFirstAnnotation.
