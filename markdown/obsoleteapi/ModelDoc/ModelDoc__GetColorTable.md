---
title: "ModelDoc::GetColorTable"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetColorTable.htm"
---

# ModelDoc::GetColorTable

This method is obsolete and has been superseded by [ModelDoc2::GetColorTable](../ModelDoc2/ModelDoc2__GetColorTable.htm) and [Sldworks::GetColorTable](sldworksAPI.chm::/SldWorks/SldWorks__GetColorTable.htm).

Description

This method returns the ColorTable object for this document.

Syntax (OLE Automation)

retval = ModelDoc.GetColorTable ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the ColorTable object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetColorTable ( &retval )

| Output: | (LPCOLORTABLE) retval | Pointer to ColorTable object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
