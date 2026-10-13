---
title: "MidSurface::GetFirstNeutralSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetFirstNeutralSheet.htm"
---

# MidSurface::GetFirstNeutralSheet

This method is obsolete and has been superseded by [MidSurface2::GetFirstNeutralSheet](sldworksAPI.chm::/MidSurface2/MidSurface2__GetFirstNeutralSheet.htm).

Description

This method return the first reference surface in this MidSurface feature. Each reference surface in the MidSurface feature is considered a sheet body. If the reference surfaces are sewn together during the creation of the MidSurface feature (ModelDoc::InsertMidSurfaceExt), then the MidSurface feature will contain only one reference surface sheet body.

Syntax (OLE Automation)

retval = MidSurface.GetFirstNeutralSheet ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the first reference surface sheet body in this MidSurface feature |
| --- | --- | --- |

Syntax (COM)

status = MidSurface->IGetFirstNeutralSheet ( &retval )

| Output: | (LPBODY) retval | First reference surface sheet body in this MidSurface feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sheet body returned from this method has the normal topology that you would expect to find on a body object (for example, faces, edges, and so on). See the Body object for the methods that provide access to this topology.
