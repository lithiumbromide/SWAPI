---
title: "Modeler::CreateConicalSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateConicalSurface.htm"
---

# Modeler::CreateConicalSurface

This method is obsolete and has been superseded by [Modeler::CreateConicalSurface2](sldworksAPI.chm::/Modeler/Modeler__CreateConicalSurface2.htm).

Description

This method creates an untrimmed conical surface from the specified arguments.

Syntax (OLE Automation)

retval = Modeler.CreateConicalSurface ( center, direction, radius, semiAngle )

| Input: | (VARIANT) center | VARIANT of type SafeArray containing 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (VARIANT) direction | VARIANT of type SafeArray containing 3 doubles (see Remarks ) |
| Input: | (double) radius | (see Remarks ) |
| Input: | (double) semiAngle | (see Remarks ) |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the resulting Surface object |

Syntax (COM)

status = Modeler->ICreateConicalSurface ( center, direction, radius, semiAngle, &retval )

| Input: | (double*) center | Pointer to an array of 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (double*) direction | Pointer to an array of 3 doubles (see Remarks ) |
| Input: | (double) radius | (see Remarks ) |
| Input: | (double) semiAngle | (see Remarks ) |
| Output: | (LPSURFACE) retval | Pointer to the resulting Surface object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The input arguments are:

- center – an XYZ location that represents the center of the bottom.
- direction – an XYZ direction of the axis of the conical surface.
- radius – the radius at the center.
- semiAngle – the half angle of the cone in radians.
