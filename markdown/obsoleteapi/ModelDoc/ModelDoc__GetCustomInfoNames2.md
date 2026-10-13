---
title: "ModelDoc::GetCustomInfoNames2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCustomInfoNames2.htm"
---

# ModelDoc::GetCustomInfoNames2

This method is obsolete and has been superseded by [ModelDoc2::GetCustomInfoNames2](../ModelDoc2/ModelDoc2__GetCustomInfoNames2.htm).

Description

This method returns a list of strings of the names of the custom properties that have been defined in the document or a specified configuration.

Syntax (OLE Automation)

retval = ModelDoc.GetCustomInfoNames2 ( configuration )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Return: | (VARIANT) retval | SafeArray of the custom property names |

Syntax (COM)

status = ModelDoc->IGetCustomInfoNames2 ( configuration, retval )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Output: | (BSTR*) retval | Array of the custom property Names. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To get the size of array needed by the COM version of this method, call ModelDoc::GetCustomInfoCount2.

File custom property information is stored in the document file. It may be general to the file, in which case there is a single value whatever the models configuration, or it may be configuration specific, in which case a different value may be set for each configuration in the model.

To access a general custom property Information value, set the configuration argument to an empty string.
