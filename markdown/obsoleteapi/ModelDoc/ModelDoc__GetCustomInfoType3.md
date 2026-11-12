---
title: "ModelDoc::GetCustomInfoType3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCustomInfoType3.htm"
---

# ModelDoc::GetCustomInfoType3

This method is obsolete and has been superseded by [ModelDoc2::GetCustomInfoType3](../ModelDoc2/ModelDoc2__GetCustomInfoType3.htm).

Description

This method returns the type of a custom information field that has been defined for this document or for the specified configuration.

Syntax (OLE Automation)

Type = ModelDoc.GetCustomInfoType3 ( configuration, FieldName )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom property |
| Return: | (long) Type | Type of custom property as defined in swCustomInfoType_e |

Syntax (COM)

status = ModelDoc->GetCustomInfoType3 ( configuration, FieldName, &Type )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom property |
| Output: | (long) Type | Type of custom property as defined in swCustomInfoType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

File custom property information is stored in the document file. It may be general to the file, in which case there is a single value whatever the models configuration, or it may be configuration specific, in which case a different value may be set for each configuration in the model.

To access a general custom property information value the configuration argument should be set to be an empty string.
