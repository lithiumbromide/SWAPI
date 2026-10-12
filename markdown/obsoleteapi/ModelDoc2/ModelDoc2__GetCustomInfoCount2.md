---
title: "ModelDoc2::GetCustomInfoCount2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCustomInfoCount2.htm"
---

# ModelDoc2::GetCustomInfoCount2

This method is obsolete and has been superseded by [ModelDocExtension::CustomPropertyManager](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CustomPropertyManager.htm).

Description

This method returns the number of custom information that have been defined for either the specified configuration or for the document.

Syntax (OLE Automation)

Count = ModelDoc2.GetCustomInfoCount2 ( configuration )

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Return: | (long) Count | Number of custom information fields |

Syntax (COM)

status = ModelDoc2->GetCustomInfoCount2 ( configuration, &Count )

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Output: | (long) Count | Number of custom information fields |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

File custom information is stored in the document file. It can be general to the file, in which case there is a single value whatever the models configuration, or it can be configuration specific, in which case a different value may be set for each configuration in the model.

To access a general custom information value, set the configuration argument to be an empty string.
