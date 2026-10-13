---
title: "ModelDoc::GetCustomInfoType2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCustomInfoType2.htm"
---

# ModelDoc::GetCustomInfoType2

This method is obsolete and has been superseded by [ModelDoc::GetCustomInfoType3](ModelDoc__GetCustomInfoType3.htm).

Description

This method returns the type of a custom information field that has been defined for this document.

Syntax (OLE Automation)

FieldType = ModelDoc.GetCustomInfoType2( FieldName )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Return: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |

Syntax (COM)

status = ModelDoc->GetCustomInfoType2( FieldName, &FieldType )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Output: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
