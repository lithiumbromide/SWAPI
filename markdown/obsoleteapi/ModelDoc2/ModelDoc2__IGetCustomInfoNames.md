---
title: "ModelDoc2::GetCustomInfoNames"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__IGetCustomInfoNames.htm"
---

# ModelDoc2::GetCustomInfoNames

This method is obsolete and has been superseded by [ModelDoc2::GetCustomInfoNames2](ModelDoc2__GetCustomInfoNames2.htm).

Description

This method returns a list of strings of the names of the custom properties that have been defined in this document.

Syntax (OLE Automation)

retval = ModelDoc2. GetCustomInfoNames( )

| Return: | (VARIANT) retval | SafeArray containing the custom property names |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetCustomInfoNames( retval )

| Output: | (BSTR*) retval | Array of the custom property names |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call ModelDoc2::GetCustomInfoCount before calling the COM version of this method.
