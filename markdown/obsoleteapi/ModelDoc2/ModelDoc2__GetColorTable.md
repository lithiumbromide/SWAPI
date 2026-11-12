---
title: "ModelDoc2::GetColorTable"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetColorTable.htm"
---

# ModelDoc2::GetColorTable

This method is obsolete and has been superseded by [Sldworks::GetColorTable](sldworksAPI.chm::/SldWorks/SldWorks__GetColorTable.htm).

Description

This method returns the ColorTable object for this document.

Syntax (OLE Automation)

retval = ModelDoc2.GetColorTable ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the ColorTable |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetColorTable ( &retval )

| Output: | (LPCOLORTABLE)retval | Pointer to ColorTable object |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
