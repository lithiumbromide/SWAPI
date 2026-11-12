---
title: "ModelDoc::GetModelViewNames"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetModelViewNames.htm"
---

# ModelDoc::GetModelViewNames

This method is obsolete and has been superseded by [ModelDoc2::GetModelViewNames](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetModelViewNames.htm).

Description

This method returns the names of the model views in this document.

Syntax (OLE Automation)

retval = ModelDoc.GetModelViewNames ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the names of all of the model views in this document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetModelViewNames ( &retval )

| Output: | (BSTR) retval | Pointer to a list of names of all of the model view in this document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
