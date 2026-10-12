---
title: "ModelDoc::GetCustomInfoType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCustomInfoType.htm"
---

# ModelDoc::GetCustomInfoType

This method is obsolete and has been superseded by [ModelDoc::GetCustomInfoType2](ModelDoc__GetCustomInfoType2.htm).

Description

This method returns the type of a custom information field that has been defined for the document.

Syntax (OLE Automation)

FieldType = ModelDoc.GetCustomInfoType( FieldName )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Return: | (BSTR) FieldType | Type of custom property |

Syntax (COM)

status = ModelDoc->GetCustomInfoType( FieldName, &FieldType )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Output: | (BSTR) FieldType | Type of custom property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The FieldType returned can be one of the following values:

- "Text"
- "Date"
- "Number"
- "Yes or no"
