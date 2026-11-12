---
title: "ModelDoc2::CustomInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CustomInfo.htm"
---

# ModelDoc2::CustomInfo

This property is obsolete and has been superseded by [ModelDoc2::CustomInfo2](ModelDoc2__CustomInfo2.htm).

Description

This property gets and sets file custom information for the SolidWorks document.

Syntax (OLE Automation)

Value = ModelDoc2.CustomInfo (fieldName) (VB Get property)

ModelDoc2. CustomInfo(fieldName) = Value (VB Set property)

Value = ModelDoc2.SetCustomInfo(fieldName) (C++ Get property)

ModelDoc2.SetCustomInfo(fieldName, Value) (C++ Set property)

| Input: | (long) fieldName | Name of field |
| --- | --- | --- |
| Property: | (BSTR) value | Text in the field |

Syntax (Com)

Status = ModelDoc.get_CustomInfo(fieldName, &Value) (C++ Get property)

Status = ModelDoc.put_CustomInfo(fieldName, Value) (C++ Set property)

| Input: | (long) fieldName | Name of field |
| --- | --- | --- |
| Property: | (BSTR) value | Text in the field |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

As per Microsoft recommendations for OLE support, the file summary information for SolidWorks documents is written as an OLE property set into a stream named "\005Summary Information" off the root storage of the SolidWorks document's compound file

NOTE: MFC does not currently provide classes that manage summary information. However, the DRAWCLI application shipped with Visual C++ does include a sample implementation, in the form of the class CSummInfo, that you can use as an example when implementing your own. This class is used by the document class CDrawDoc. DRAWCLI also includes property pages for displaying and modifying summary information.
