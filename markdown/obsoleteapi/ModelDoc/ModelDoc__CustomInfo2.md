---
title: "ModelDoc::CustomInfo2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CustomInfo2.htm"
---

# ModelDoc::CustomInfo2

This property is obsolete and has been superseded by [ModelDoc2::CustomInfo2](../ModelDoc2/ModelDoc2__CustomInfo2.htm).

Description

This property gets and sets the file custom information for the SolidWorks document.

Syntax (OLE Automation)

value = ModelDoc.CustomInfo2 (configuration, fieldName) (VB Get property)

ModelDoc. CustomInfo2(configuration, fieldName) = value (VB Set property)

value = ModelDoc.GetCustomInfo2(configuration, fieldName) (C++ Get property)

ModelDoc.SetCustomInfo2(configuration, fieldName, value) (C++ Set property)

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) fieldName | Name of field |
| Property: | (BSTR) value | Text in the field |

Syntax (Com)

status = ModelDoc.get_CustomInfo2(configuration, fieldName, &value) (C++ Get property)

status = ModelDoc.put_CustomInfo2(configuration, fieldName, value) (C++ Set property)

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) fieldName | Name of field |
| Property: | (BSTR) value | Text in the field |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

File custom property information is stored in the document file. It may be general to the file, in which case there is a single value whatever the model's configuration, or it may be configuration specific, in which case a different value may be set for each configuration in the model.

To access a general custom property information value the configuration argument should be set to be an empty string.

In line with Microsoft recommendations for OLE support, the file summary information for SolidWorks documents is written as an OLE property set into a stream named "\005Summary Information" off the root storage of the SolidWorks document's compound file

NOTE: MFC does not currently provide classes that manage summary information. However, the DRAWCLI application shipped with Visual C++ does include a sample implementation, in the form of the class CSummInfo, which you can use as an example when implementing your own. This class is used by the document class CDrawDoc. DRAWCLI also includes property pages for displaying and modifying summary information.
