---
title: "ModelDoc2::AddCustomInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddCustomInfo.htm"
---

# ModelDoc2::AddCustomInfo

This method is obsolete and has been superseded by [ModelDoc2::AddCustomInfo2](ModelDoc2__AddCustomInfo2.htm).

Description

This method adds a custom info field to the document.

Syntax (OLE Automation)

retval = ModelDoc2.AddCustomInfo( FieldName, FieldType, FieldValue )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (BSTR) FieldType | Type of custom property |
| Input: | (BSTR) FieldValue | Value of custom property |
| Return: | (BOOL) retval | TRUE if added, FALSE if not |

Syntax (COM)

status = ModelDoc2->AddCustomInfo( FieldName, FieldType, FieldValue, &retval )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (BSTR) FieldType | Type of custom property |
| Input: | (BSTR) FieldValue | Value of custom property |
| Output: | (VARIANT_BOOL) retval | TRUE if added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The FieldType argument can be one of the following values:

- "Text"
- "Date"
- "Number"
- "Yes or no"
