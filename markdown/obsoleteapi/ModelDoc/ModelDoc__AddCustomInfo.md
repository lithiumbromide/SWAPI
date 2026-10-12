---
title: "ModelDoc::AddCustomInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddCustomInfo.htm"
---

# ModelDoc::AddCustomInfo

This method is obsolete and has been superseded by [ModelDoc::AddCustomInfo2](ModelDoc__AddCustomInfo2.htm).

Description

This method adds a custom property field to the document.

Syntax (OLE Automation)

retval = ModelDoc.AddCustomInfo( FieldName, FieldType, FieldValue )

| Input: | (BSTR)FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (BSTR)FieldType | Type of custom property |
| Input: | (BSTR)FieldValue | Value of custom property |
| Return: | (BOOL)retval | TRUE if added |

Syntax (COM)

status = ModelDoc->AddCustomInfo( FieldName, FieldType, FieldValue, &retval )

| Input: | (BSTR)FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (BSTR)FieldType | Type of custom property |
| Input: | (BSTR)FieldValue | Value of custom property |
| Output: | (VARIANT_BOOL)retval | TRUE if added, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The FieldType argument can be one of these values:

- "Text"
- "Date"
- "Number"
- "Yes or no"
