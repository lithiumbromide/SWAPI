---
title: "Body::CreateBoundedSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBoundedSurface.htm"
---

# Body::CreateBoundedSurface

This method is obsolete and has been superseded by [Body2::CreateBoundedSurface](sldworksAPI.chm::/Body2/Body2__CreateBoundedSurface.htm).

Description

This method creates a bounded surface from an independent base surface.

Syntax (OLE Automation)

retval = Body.CreateBoundedSurface ( uOpt, vOpt, uvParams)

| Input: | (BOOL) uOpt | TRUE if the U parameter range is given in uvData, FALSE if the entire U parameter range is used |
| --- | --- | --- |
| Input: | (BOOL) vOpt | TRUE if the V parameter range is given in uvData, FALSE if the entire V parameter range is used |
| Input: | (VARIANT) uvParams | VARIANT of type SafeArray of 4 doubles |
| Return: | (BOOL) retval | TRUE if bounded surface creation was successful, FALSE if it was not |

Syntax (COM)

status = Body->ICreateBoundedSurface ( UOpt, VOpt, UVParams )

| Input: | (VARIANT_BOOL) UOpt | TRUE if the U parameter range is given in uvData, FALSE if the entire U parameter range is used |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) VOpt | TRUE if the V parameter range is given in uvData, FALSE if the entire V parameter range is used |
| Input: | (double*) UVParams | An array of 4 doubles |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Before you call this method, you must call one of the base surface creation methods, such as Body::CreateBsplineSurface.

The UOpt and VOpt arguments allow the you to supply parameter range information so that you can create a bounded surface from part of the base surface. If both uOpt and vOpt are set to FALSE, then SolidWorks uses the entire parameter ranges. SolidWorks cannot do this for surfaces with infinite parameter ranges.

UVParams contains 4 doubles describing the UV parameter ranges.

- U parameter range is supplied in uvData[0] and uvData[1]. UvData[0] must be less than uvData[1].
- V parameter range is supplied in uvData[2] and uvData[3]. UvData[2] must be less than uvData[3].

If you want to construct a solid body from bounded surfaces, then you must first call PartDoc::CreateNewBody, which arranges for a placeholder for this bounded surface.
