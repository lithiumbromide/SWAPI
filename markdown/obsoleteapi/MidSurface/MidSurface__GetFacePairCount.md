---
title: "MidSurface::GetFacePairCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetFacePairCount.htm"
---

# MidSurface::GetFacePairCount

This method is obsolete and has been superseded by [MidSurface2::GetFacePairCount](sldworksAPI.chm::/MidSurface2/MidSurface2__GetFacePairCount.htm).

Description

This method will get the number of parallel pairs of faces found in the original part body that were used to calculate the MidSurface feature.

Syntax (OLE Automation)

retval = MidSurface.GetFacePairCount ()

| Return: | (long) retval | Number of parallel face pairs from the original part body. |
| --- | --- | --- |

Syntax (COM)

status = MidSurface->GetFacePairCount ( &retval )

| Output: | (long) retval | Number of parallel face pairs from the original part body. |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
