---
title: "Modeler::CreateCylindricalSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateCylindricalSurface.htm"
---

# Modeler::CreateCylindricalSurface

This method is obsolete and has been superseded by [Modeler::CreateCylindricalSurface2](sldworksAPI.chm::/Modeler/Modeler__CreateCylindricalSurface2.htm).

Description

This method creates an untrimmed cylindrical surface from the specified arguments.

Syntax (OLE Automation)

retval = Modeler.CreateCylindricalSurface ( center, direction, radius )

| Input: | (VARIANT) center | VARIANT of type SafeArray containing 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (VARIANT) direction | VARIANT of type SafeArray containing 3 doubles (see Remarks ) |
| Input: | (double) radius | See Remarks |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the resulting Surface object |

Syntax (COM)

status = Modeler->ICreateCylindricalSurface ( center, direction, radius, &retval )

| Input: | (double*) center | Pointer to an array of 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (double*) direction | Pointer to an array of 3 doubles (see Remarks ) |
| Input: | (double) radius | See Remarks |
| Output: | (LPSURFACE) retval | Pointer to the resulting Surface object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Input arguments:

- center – an XYZ location which represents the center of the bottom.
- direction – an XYZ direction of the axis of the cylindrical surface.
- radius – the radius at the center.
