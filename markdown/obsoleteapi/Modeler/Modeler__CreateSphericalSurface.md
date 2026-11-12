---
title: "Modeler::CreateSphericalSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateSphericalSurface.htm"
---

# Modeler::CreateSphericalSurface

This method is obsolete and has been superseded by [Modeler::CreateSphericalSurface2](sldworksAPI.chm::/Modeler/Modeler__CreateSphericalSurface2.htm).

Description

This method creates an untrimmed spherical surface from the specified arguments.

Syntax (OLE Automation)

retval = Modeler.CreateSphericalSurface ( center, radius )

| Input: | (VARIANT) center | VARIANT of type SafeArray containing 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (double) radius | See Remarks |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the resulting surface |

Syntax (COM)

status = Modeler->ICreateSphericalSurface ( center, radius, &retval )

| Input: | (double*) center | Pointer to an array of 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (double) radius | See Remarks |
| Output: | (LPSURFACE) retval | Pointer to the resulting surface |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Input arguments:

- center – an XYZ location which represents the center of the spherical surface.
- radius – the radius at the center.

You can trim the resulting surface can be trimmed using, for example, Surface::CreateTrimmedSheet, to generate a sheet body.
