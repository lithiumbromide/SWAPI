---
title: "ModelDoc2::GetDetailingDefaults"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetDetailingDefaults.htm"
---

# ModelDoc2::GetDetailingDefaults

This method is obsolete and has been superseded by [ModelDoc2::GetUserPreferenceTextFormat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceTextFormat.htm) and [ModelDoc2::SetUserPreferenceTextFormat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ISetUserPreferenceTextFormat.htm).

Description

This method gets the detailing defaults for this document

Syntax (OLE Automation)

retval = ModelDoc2.GetDetailingDefaults( )

| Return: | (LPDISPATCH) retval | Dispatch Pointer for the DetailingDefaults object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetDetailingDefaults( &retval )

| Output: | (LPDETAILINGDEFAULTS) retval | Pointer to the DetailingDefaults object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
