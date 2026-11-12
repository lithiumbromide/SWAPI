---
title: "ModelDoc::GetSceneBkgDIB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetSceneBkgDIB.htm"
---

# ModelDoc::GetSceneBkgDIB

This method is obsolete and has been superseded by [ModelDoc2::GetSceneBkgDIB](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetSceneBkgDIB.htm).

Description

This method gets background image as a LPDIBSECTION.

Syntax (OLE Automation)

l_dib = ModelDoc.GetSceneBkgDIB ( )

| Return: | (long) l_dib | Background image as DIBSECTION |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetSceneBkgDIB ( &l_dib )

| Output: | (long)l_dib | Background image as DIBSECTION |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For more information, see Bitmap structures, DIBSECTION in MicroSoft Help.

The memory for the image bits ( DIBSECTION.dsBm.bmBits) and this structure are allocated by SolidWorks and must be deleted by the caller.
