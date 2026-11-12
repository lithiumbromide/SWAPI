---
title: "MidSurface::GetNextNeutralSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetNextNeutralSheet.htm"
---

# MidSurface::GetNextNeutralSheet

This method is obsolete and has been superseded by [MidSurface2::GetNextNeutralSheet](sldworksAPI.chm::/MidSurface2/MidSurface2__GetNextNeutralSheet.htm).

Description

This method returns the next reference surface in this MidSurface feature. Each reference surface in the MidSurface feature is considered a sheet body. If the reference surfaces are sewn together during the creation of the MidSurface feature (ModelDoc::InsertMidSurfaceExt), then the MidSurface feature will contain only one reference surface sheet body. If this is the case, then this method returns NULL. The first and only reference surface sheet body should have been returned with the MidSurface::GetFirstNeutralSheet method.

Syntax (OLE Automation)

retval = MidSurface.GetNextNeutralSheet ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the next reference surface sheet body in this MidSurface feature |
| --- | --- | --- |

Syntax (COM)

status = MidSurface->IGetNextNeutralSheet ( &retval )

| Output: | (LPBODY) retval | Next reference surface sheet body in this MidSurface feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sheet body returned from this method has the normal topology that you would expect to find on a body object (for example, faces, edges, and son). See the Body object for the methods that provide access to this topology.
