---
title: "ModelDoc::GetCustomInfoNames"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCustomInfoNames.htm"
---

# ModelDoc::GetCustomInfoNames

This method is obsolete and has been superseded by [ModelDoc2::GetCustomInfoNames](../ModelDoc2/ModelDoc2__IGetCustomInfoNames.htm).

Description

This method returns a list of strings of the names of the custom properties that have been defined in this document.

Syntax (OLE Automation)

retval = ModelDoc. GetCustomInfoNames( )

| Return: | (VARIANT) retval | SafeArray of the custom property names |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetCustomInfoNames( retval )

| Output: | (BSTR*) retval | Array of the custom property names |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To get the size of array needed by the COM version of this method, call ModelDoc::GetCustomInfoCount.
