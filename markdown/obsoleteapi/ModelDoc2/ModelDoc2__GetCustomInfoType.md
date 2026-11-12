---
title: "ModelDoc2::GetCustomInfoType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCustomInfoType.htm"
---

# ModelDoc2::GetCustomInfoType

This method is obsolete and has been superseded by [ModelDoc2::GetCustomInfoType2](ModelDoc2__GetCustomInfoType2.htm).

Description

This method returns the type of a custom info field that has been defined for the document.

Syntax (OLE Automation)

FieldType = ModelDoc2.GetCustomInfoType( FieldName )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Return: | (BSTR) FieldType | Type of custom property |

Syntax (COM)

status = ModelDoc2->GetCustomInfoType( FieldName, &FieldType )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Output: | (BSTR) FieldType | Type of custom property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

FieldType returned can be one of the following values:

- "Text"
- "Date"
- "Number"
- "Yes or no"
