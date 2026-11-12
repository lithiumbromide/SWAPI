---
title: "ModelDoc2::AddCustomInfo3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddCustomInfo3.htm"
---

# ModelDoc2::AddCustomInfo3

This method is obsolete and has been superseded by [ModelDocExtension::CustomPropertyManager](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CustomPropertyManager.htm).

Description

This method adds a custom property to the document or to the specified configuration.

Syntax (OLE Automation)

retval = ModelDoc2.AddCustomInfo3 ( configuration, FieldName, FieldType, FieldValue )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom property |
| Input: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Input: | (BSTR) FieldValue | Value of custom property |
| Return: | (BOOL) retval | TRUE if added, FALSE if not |

Syntax (COM)

status = ModelDoc2->AddCustomInfo3 ( configuration, FieldName, FieldType, FieldValue, &retval )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom property |
| Input: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Input: | (BSTR) FieldValue | Value of custom property |
| Output: | (VARIANT_BOOL) retval | TRUE if added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A file custom property is stored in the document file. It can be:

- general to the file, in which case there is a single value whatever the model's configuration
- specific to the configuration, in which case a different value can be set for each configuration in the model.

To access a general custom property value, set the configuration argument to an empty string.

Because drawing documents do not support configurations, set the configuration argument to an empty string.
