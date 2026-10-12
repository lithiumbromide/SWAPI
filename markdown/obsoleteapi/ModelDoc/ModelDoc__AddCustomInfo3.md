---
title: "ModelDoc::AddCustomInfo3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddCustomInfo3.htm"
---

# ModelDoc::AddCustomInfo3

This method is obsolete and has been superseded by [ModelDoc2::AddCustomInfo3](../ModelDoc2/ModelDoc2__AddCustomInfo3.htm).

Description

This method adds a custom property field to the document or the specified configuration.

Syntax (OLE Automation)

retval = ModelDoc.AddCustomInfo3 ( configuration, FieldName, FieldType, FieldValue )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom property |
| Input: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Input: | (BSTR) FieldValue | Value of custom property |
| Return: | (BOOL) retval | TRUE if added, FALSE if not |

Syntax (COM)

status = ModelDoc->AddCustomInfo3 ( configuration, FieldName, FieldType, FieldValue, &retval )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom property |
| Input: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Input: | (BSTR) FieldValue | Value of custom property |
| Output: | (VARIANT_BOOL) retval | TRUE if added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

File custom property information is stored in the document file. It may be general to the file, in which case there is a single value whatever the models configuration, or it may be configuration specific, in which case a different value may be set for each configuration in the model.

To access a general custom property information value, set the configuration argument sto be an empty string.
