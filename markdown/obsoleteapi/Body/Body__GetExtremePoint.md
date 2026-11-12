---
title: "Body::GetExtremePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetExtremePoint.htm"
---

# Body::GetExtremePoint

This method is obsolete and has been superseded by [Body2::GetExtremePoint](sldworksAPI.chm::/Body2/Body2__GetExtremePoint.htm).

Description

This method calculates the extreme point of the model in the given direction.

Syntax (OLE Automation)

retval = Body.GetExtremePoint ( x, y, z, &outx, &outy, &outz )

| Input: | (double) x | X component of the direction vector |
| --- | --- | --- |
| Input: | (double) y | Y component of the direction vector |
| Input: | (double) z | Z component of the direction vector |
| Output: | (double) outx | Extreme point X coordinate |
| Output: | (double) outy | Extreme point Y coordinate |
| Output: | (double) outz | Extreme point Z coordinate |
| Return: | (BOOL) retval | TRUE if a point was found, FALSE if it was not |

Syntax (COM)

status = Body->GetExtremePoint ( x, y, z, &outx, &outy, &outz, &found )

| Input: | (double) x | X component of the direction vector |
| --- | --- | --- |
| Input: | (double) y | Y component of the direction vector |
| Input: | (double) z | Z component of the direction vector |
| Output: | (double) outx | Extreme point X coordinate |
| Output: | (double) outy | Extreme point Y coordinate |
| Output: | (double) outz | Extreme point Z coordinate |
| Output: | (VARIANT_BOOL) found | TRUE if a point was found, FALSE if it was not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the furthest possible intersection point between a plane normal to the specified direction vector and the model, as the plane moves along the direction vector.

For example, if the model is a right cube centered on the origin and the direction vector is (1.0, 1.0, 1.0), then the extreme point is the vertex at (1.0, 1.0, 1.0).

If there is more than one point (for example, if there is a face perpendicular to the direction vector), then SolidWorks returns a unique point found in a deterministic way.
