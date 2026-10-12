---
title: "MidSurface::GetFirstFacePair"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetFirstFacePair.htm"
---

# MidSurface::GetFirstFacePair

This method is obsolete and has been superseded by [MidSurface2::GetFirstFacePair](sldworksAPI.chm::/MidSurface2/MidSurface2__GetFirstFacePair.htm).

Description

This method returns the first face pair in this MidSurface feature along with the thickness (in meters) between the two faces. The two face objects returned are the two parallel faces from the original part body that were used to generate the first neutral face in this MidSurface feature.

Syntax (OLE Automation)

retval = MidSurface.GetFirstFacePair ( &thickness, &partnerFaceDisp)

| Output: | (double) thickness | Distance between the two parallel faces, from Face1 and from Face2 |
| --- | --- | --- |
| Output: | (LPDISPATCH) partnerFaceDisp | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |

Syntax (COM)

status = MidSurface->IGetFirstFacePair ( &thickness, &partnerFaceDisp, &retval )

| Output: | (double) thickness | Distance between the two parallel faces, fromFace1 and fromFace2 |
| --- | --- | --- |
| Output: | (LPFACE) partnerFaceDisp | Pointer to a face on the original part body used in generating the neutral face |
| Output: | (LPFACE) retval | Pointer to a face on the original part body used in generating the neutral face |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is identical to MidSurface::GetFirstFace except this method does not return the neutral face.
