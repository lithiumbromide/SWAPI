---
title: "Tessellation::IGetFaceFacetsCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Tessellation/Tessellation__IGetFaceFacetsCount.htm"
---

# Tessellation::IGetFaceFacetsCount

This method is obsolete and has been superseded by [Tessellation::IGetFaceFacetsCount2](sldworksAPI.chm::/Tessellation/TESSELLATION__IGETFACEFACETSCOUNT2.HTM).

Description

This method gets the number of facets corresponding to a face.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Tessellation->IGetFaceFacetsCount ( faceObj, &retval )

| Input: | (LPFACE) faceObj | Face on which to count facets |
| --- | --- | --- |
| Output: | (long) retval | Number of facets on Face object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
