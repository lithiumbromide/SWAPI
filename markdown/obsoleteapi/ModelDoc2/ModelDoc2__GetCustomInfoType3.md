---
title: "ModelDoc2::GetCustomInfoType3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCustomInfoType3.htm"
---

# ModelDoc2::GetCustomInfoType3

This method is obsolete and has been superseded by [ModelDocExtension::CustomPropertyManager](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CustomPropertyManager.htm).

Description

This method returns the type of custom information that has been defined for the document or for the specified configuration.

Syntax (OLE Automation)

Type = ModelDoc2.GetCustomInfoType3 ( configuration, FieldName )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom information |
| Return: | (long) Type | Type of custom information as defined in swCustomInfoType_e |

Syntax (COM)

status = ModelDoc2->GetCustomInfoType3 ( configuration, FieldName, &Type )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom information |
| Output: | (long) Type | Type of custom information as defined in swCustomInfoType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

File custom information is stored in the document file. It can be general to the file, in which case there is a single value whatever the models configuration, or it can be configuration specific, in which case a different value may be set for each configuration in the model.

To access a general custom information value, set the configuration argument to be an empty string.
