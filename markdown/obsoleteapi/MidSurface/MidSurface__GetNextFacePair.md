---
title: "MidSurface::GetNextFacePair"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetNextFacePair.htm"
---

# MidSurface::GetNextFacePair

This method is obsolete and has been superseded by [MidSurface2::GetNextFacePair](sldworksAPI.chm::/MidSurface2/MidSurface2__GetNextFacePair.htm).

Description

This method returns the next face pair in this MidSurface feature along with the thickness (in meters) between the two faces. The two face objects returned are the two parallel faces from the original part body that were used to generate the neutral face in this MidSurface feature.

Syntax (OLE Automation)

retval = MidSurface.GetNextFacePair ( &thickness, &partnerFaceDisp)

| Output: | (double) thickness | Distance between the two parallel faces |
| --- | --- | --- |
| Output: | (LPDISPATCH) partnerFaceDisp | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a face on the original part body used in generating the neutral face |

Syntax (COM)

status = MidSurface->IGetNextFacePair ( &thickness, &partnerFace, &retval )

| Output: | (double) thickness | Distance between the two parallel faces |
| --- | --- | --- |
| Output: | (LPFACE) partnerFace | Pointer a face on the original part body used in generating the neutral face |
| Output: | (LPFACE) retval | Pointer a face on the original part body used in generating the neutral face |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used in combination with MidSurface::GetFirstFacePair. Each time this method is called, it returns subsequent face pairs used in this MidSurface feature.

This method is identical to MidSurface::GetNextFace except this method does not return the neutral face.
