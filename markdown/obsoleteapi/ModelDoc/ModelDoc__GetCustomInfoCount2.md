---
title: "ModelDoc::GetCustomInfoCount2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCustomInfoCount2.htm"
---

# ModelDoc::GetCustomInfoCount2

This method is obsolete and has been superseded by [ModelDoc2::GetCustomInfoCount2](../ModelDoc2/ModelDoc2__GetCustomInfoType2.htm).

Description

This method returns the number of custom information fields that have been defined for either the specified configuration or for the document.

Syntax (OLE Automation)

Count = ModelDoc.GetCustomInfoCount2 ( configuration )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Return: | (long) Count | Number of custom information fields |

Syntax (COM)

status = ModelDoc->GetCustomInfoCount2 ( configuration, &Count )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Output: | (long) Count | Number of custom information fields |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

File custom property information is stored in the document file. It may be general to the file, in which case there is a single value whatever the models configuration, or it may be configuration specific, in which case a different value may be set for each configuration in the model.

To access a general custom property information value, set the configuration argument to an empty string.
