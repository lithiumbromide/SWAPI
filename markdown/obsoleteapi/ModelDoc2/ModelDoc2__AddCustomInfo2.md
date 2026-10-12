---
title: "ModelDoc2::AddCustomInfo2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddCustomInfo2.htm"
---

# ModelDoc2::AddCustomInfo2

This method is obsolete and has been superseded by [ModelDoc2::AddCustomInfo3](ModelDoc2__AddCustomInfo3.htm).

Description

This method adds a custom information field to the document.

Syntax (OLE Automation)

retval = ModelDoc2.AddCustomInfo2( FieldName, FieldType, FieldValue )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Input: | (BSTR) FieldValue | Value of custom property |
| Return: | (BOOL) retval | TRUE if added, FALSE if not |

Syntax (COM)

status = ModelDoc2->AddCustomInfo2( FieldName, FieldType, FieldValue, &retval )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Input: | (BSTR) FieldValue | Value of dustom property |
| Output: | (VARIANT_BOOL) retval | TRUE if added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
