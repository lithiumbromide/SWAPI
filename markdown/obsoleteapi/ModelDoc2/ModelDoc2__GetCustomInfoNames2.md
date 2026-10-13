---
title: "ModelDoc2::GetCustomInfoNames2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCustomInfoNames2.htm"
---

# ModelDoc2::GetCustomInfoNames2

This method is obsolete and has been superseded by [ModelDocExtension::CustomPropertyManager](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CustomPropertyManager.htm).

Description

This method returns the names of the custom information defined in the document or a specified configuration.

Syntax (OLE Automation)

retval = ModelDoc2.GetCustomInfoNames2 ( configuration )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Return: | (VARIANT) retval | SafeArray containing the names of the custom information |

Syntax (COM)

status = ModelDoc2->IGetCustomInfoNames2 ( configuration, retval )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Output: | (BSTR*) retval | Array containing the names of the custom information |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call ModelDoc2::GetCustomInfoCount2 before calling the COM version of this method.

File custom information is stored in the document file. It can be general to the file, in which case there is a single value whatever the configuration of the model, or it can be configuration specific, in which case a different value may be set for each configuration in the model.

To access a general custom information value, set the configuration argument to an empty string.
