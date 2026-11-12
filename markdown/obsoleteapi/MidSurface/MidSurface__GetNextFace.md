---
title: "MidSurface::GetNextFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetNextFace.htm"
---

# MidSurface::GetNextFace

This method is obsolete and has been superseded by [MidSurface2::GetNextFace](sldworksAPI.chm::/MidSurface2/MidSurface2__GetNextFace.htm).

Description

This method is used in combination with MidSurface::GetFirstFace. Each time this method is called, it returns subsequent faces in this MidSurface feature.

Syntax (OLE Automation)

retval = MidSurface.GetNextFace ( fromFace1Disp, fromFace2Disp, thickness)

| Output: | (LPDISPATCH) fromFace1Disp | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |
| --- | --- | --- |
| Output: | (LPDISPATCH) fromFace2Disp | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |
| Output: | (double) thickness | Distance between the two parallel faces, Face1 and Face2 |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a face in this MidSurface feature |

Syntax (COM)

status = MidSurface->IGetNextFace ( fromFace1Disp, fromFace2Disp, thickness, &retval )

| Output: | (LPFACE) fromFace1Disp | Pointer a face on the original part body used in generating the neutral face |
| --- | --- | --- |
| Output: | (LPFACE) fromFace2Disp | Pointer a face on the original part body used in generating the neutral face |
| Output: | (double) thickness | Distance between the two parallel faces, Face1 and Face2 |
| Output: | (LPFACE) retval | Face in this MidSurface feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the next neutral face in this MidSurface feature along with three other items. The first two return values are the two faces from the original part body that were used to generate this neutral MidSurface face. The next return value is the thickness (in meters) between the two parallel faces from the original part body. The last return value is the neutral face in this MidSurface feature.
