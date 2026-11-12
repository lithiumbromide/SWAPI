---
title: "Body::CreateBlendSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBlendSurface.htm"
---

# Body::CreateBlendSurface

This method is obsolete and has been superseded by [Body2::CreateBlendSurface](sldworksAPI.chm::/Body2/Body2__CreateBlendSurface.htm).

Description

This method creates a constant radius rolling ball blend surface (also known as a pipe surface) between two side surfaces. The surface generated is the path traced out when a sphere of the blend radius is rolled in contact with the two side surfaces. The center of the sphere rolls along the spine, which is the intersection of these two surfaces when offset by the blend radius.

Syntax (OLE Automation)

retval = Body.CreateBlendSurface ( Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec, HaveHelpBox, HelpBox)

| Input: | (LPDISPATCH) Surface1 | Dispatch pointer to the first side surface |
| --- | --- | --- |
| Input: | (double) Range1 | Signed offset of Surface1 |
| Input: | (LPDISPATCH) Surface2 | Dispatch pointer to the second side surface |
| Input: | (double) Range2 | Signed offset of Surface2 |
| Input: | (VARIANT) StartVec | VARIANT of type SafeArray of 3 doubles representing a point close to the tart of the blend spine |
| Input: | (VARIANT) EndVec | VARIANT of type SafeArray of 3 doubles representing a point close to the end of the blend spine |
| Input: | (int) HaveHelpVec | Optional boolean if help vector is provided |
| Input: | (VARIANT) HelpVec | VARIANT of type SafeArray of 3 doubles representing the direction of the Help vector |
| Input: | (int) HaveHelpBox | Optional Boolean if box is provided |
| Input: | (VARIANT) HelpBox | VARIANT of type SafeArray of 6 doubles bounding the area of interest |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created surface |

Syntax (COM)

status = Body->ICreateBlendSurface ( Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec, HaveHelpBox, HelpBox, &retval )

| Input: | (LPSURFACE) Surface1 | Pointer to the first side surface |
| --- | --- | --- |
| Input: | (double) Range1 | Signed offset of Surface1 |
| Input: | (LPSURFACE) Surface2 | Pointer to the second side surface |
| Input: | (double) Range2 | Signed offset of Surface2 |
| Input: | (double*) StartVec | Array of 3 doubles representing a point close to the start of the blend spine |
| Input: | (double*) EndVec | Array of 3 doubles representing a point close to the end of the blend spine |
| Input: | (int) HaveHelpVec | Optional Boolean if help vector is provided |
| Input: | (double*) HelpVec | Array of 3 doubles representing the direction of the Help vector. |
| Input: | (int) HaveHelpBox | Optional boolean if box is provided |
| Input: | (double*) HelpBox | Array of 6 doubles bounding the area of interest |
| Output: | (LPSURFACE) retval | Pointer to the newly created surface. |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
