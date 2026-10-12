---
title: "MidSurface::GetNeutralSheetCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetNeutralSheetCount.htm"
---

# MidSurface::GetNeutralSheetCount

This method is obsolete and has been superseded by [MidSurface2::GetNeutralSheetCount](sldworksAPI.chm::/MidSurface2/MidSurface2__GetNeutralSheetCount.htm).

Description

This method determines the total number of reference surfaces found in this MidSurface feature. Each reference surface in the MidSurve feature is considered a sheet body. If the reference surfaces are sewn together during the creation of the MidSurface feature (ModelDoc::InsertMidSurfaceExt), then the MidSurface feature will contain only one reference surface sheet body.

Syntax (OLE Automation)

retval = MidSurface.GetNeutralSheetCount ()

| Return: | (long) retval | Number of reference surface sheet bodies found in this MidSurface feature |
| --- | --- | --- |

Syntax (COM)

status = MidSurface->GetNeutralSheetCount ( &retval )

| Output: | (long) retval | Number of reference surface sheet bodies found in this MidSurface feature |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
