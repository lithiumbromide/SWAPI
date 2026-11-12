---
title: "Surface::IGetBSurfParamsSize2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__IGetBSurfParamsSize2.htm"
---

# Surface::IGetBSurfParamsSize2

This method has been superseded by [Surface::IGetBSurfParamsSize3](sldworksAPI.chm::/Surface/Surface__IGetBSurfParamsSize3.htm).

Description

This method gets the allocation size necessary for Bsurface parameter data retrieval in a subsequent call to Surface::GetBSurfParams.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Surface->IGetBSurfParamsSize2 (wantCubic, wantNonRational, range, &retval )

| Input: | (VARIANT_BOOL) wantCubic | TRUE for surface to be a cubic, FALSE otherwise |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) wantNonRational | TRUE for surface to be rational, FALSE otherwise |
| Input: | (double*) range | Pointer to an array of 4 doubles describing the U,V Range; the four values are upper and lower U and V bounds respectively; these values can be obtained using Surface::Parameterization. |
| Output: | (long) retval | Size of the data set |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Range contains the following values, which can be obtained using Surface::Parameterization:

- Range[0] & Range[2] are the lower bounds of the U & V surface parameters, respectively.
- Range[1] & Range[3] are the upper bounds of the U & V surface parameters, respectively.
