---
title: "ModelDoc::SummaryInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SummaryInfo.htm"
---

# ModelDoc::SummaryInfo

This property is obsolete and has been superseded by [ModelDoc2::SummaryInfo](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SummaryInfo.htm).

Description

This property gets and sets file summary information for the SolidWorks document.

Syntax (OLE Automation)

value = ModelDoc.SummaryInfo ( fieldId ) (VB Get property)

ModelDoc.SummaryInfo ( fieldId ) = value (VB Set property)

value = ModelDoc.GetSummaryInfo ( fieldId) (C++ Get property)

ModelDoc.SetSummaryInfo ( fieldId, value) (C++ Set property)

| Input: | (long) fieldId | Identifier as defined in swSummInfoField_e |
| --- | --- | --- |
| Property: | (BSTR) value | Text |

Syntax (Com)

Status = ModelDoc.get_SummaryInfo ( fieldId &value) (C++ Get property)

Status = ModelDoc.put_SummaryInfo ( fieldId, value) (C++ Set property)

| Input: | (long) fieldId | Identifier as defined in swSummInfoField_e |
| --- | --- | --- |
| Property: | (BSTR) value | Text |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

In line with Microsoft recommendations for OLE support, the file summary information for SolidWorks documents is written as an OLE property set into a stream named "\005Summary Information" off the root storage of the SolidWorks document's compound file.

NOTE: MFC does not currently provide classes that manage summary information. However, the DRAWCLI application shipped with Visual C++ does include a sample implementation, in the form of the class CSummInfo, which you can use as an example when implementing your own. This class is used by the document class CDrawDoc. DRAWCLI also includes property pages for displaying and modifying summary information.
