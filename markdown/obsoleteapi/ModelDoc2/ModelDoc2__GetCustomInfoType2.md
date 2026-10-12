---
title: "ModelDoc2::GetCustomInfoType2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCustomInfoType2.htm"
---

# ModelDoc2::GetCustomInfoType2

This method is obsolete and has been superseded by [ModelDoc2::GetCustomInfoType3](ModelDoc2__GetCustomInfoType3.htm).

Description

Returns the type of a custom info field that has been defined for the document.

Syntax (OLE Automation)

FieldType = ModelDoc2.GetCustomInfoType2( FieldName )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Return: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |

Syntax (COM)

status = ModelDoc2->GetCustomInfoType2( FieldName, &FieldType )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Output: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
