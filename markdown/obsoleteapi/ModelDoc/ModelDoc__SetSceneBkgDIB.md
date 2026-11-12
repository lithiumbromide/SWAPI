---
title: "ModelDoc::SetSceneBkgDIB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetSceneBkgDIB.htm"
---

# ModelDoc::SetSceneBkgDIB

This method is obsolete and has been superseded by [ModelDoc2::SetSceneBkgDIB](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetSceneBkgDIB.htm).

Description

This sets background image described by DIBSECTION data.

Syntax (OLE Automation)

(void) ModelDoc.SetSceneBkgDIB ( l_dib )

| Input: | (long) l_dib | Pointer to DIBSECTION |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetSceneBkgDIB ( l_dib )

| Input: | (long) l_dib | Pointer to DIBSECTION |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For more information, see the description of bitmap structures in MicroSoft Help.

Old background images are deleted automatically.
