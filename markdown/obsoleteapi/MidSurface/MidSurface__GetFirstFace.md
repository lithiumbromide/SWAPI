---
title: "MidSurface::GetFirstFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetFirstFace.htm"
---

# MidSurface::GetFirstFace

This method is obsolete and has been superseded by [MidSurface2::GetFirstFace](sldworksAPI.chm::/MidSurface2/MidSurface2__GetFirstFace.htm).

Description

This method returns the first face in this MidSurface feature along with three other items. The first two return values are the two faces from the original part body that were used to generate this MidSurface face. The next return value is the thickness (in meters) between the two parallel faces from the original part body. The last return value is the first face in this MidSurface feature.

Syntax (OLE Automation)

retval = MidSurface.GetFirstFace ( &fromFace1Disp, &fromFace2Disp, &thickness)

| Output: | (LPDISPATCH) fromFace1Disp | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |
| --- | --- | --- |
| Output: | (LPDISPATCH) fromFace2Disp | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |
| Output: | (double) thickness | Distance between the two parallel faces, fromFace1Disp and fromFace2Disp |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the first face in this MidSurface feature |

Syntax (COM)

status = MidSurface->IGetFirstFace ( &fromFace1Disp, &fromFace2Disp, &thickness, &retval )

| Output: | (LPFACE) fromFace1Disp | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |
| --- | --- | --- |
| Output: | (LPFACE) fromFace2Disp | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |
| Output: | (double) thickness | Distance between the two parallel faces, fromFace1Disp and fromFace2Disp |
| Output: | (LPFACE) retval | First face in this MidSurface feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
