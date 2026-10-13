---
title: "Body::SetCurrentSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__SetCurrentSurface.htm"
---

# Body::SetCurrentSurface

This method is obsolete and has been superseded by [Body2::SetCurrentSurface](sldworksAPI.chm::/Body2/Body2__SetCurrentSurface.htm).

Description

This method places an existing surface object into a temporary body object that is under construction.

Syntax (OLE Automation)

void Body.SetCurrentSurface ( surfaceIn )

| Input: | (LPDISPATCH) surfaceIn | Pointer to a Dispatch object, a surface; this surface might have been created using other surface creation routines, such as Modeler::CreateCylindricalSurface |
| --- | --- | --- |

Syntax (COM)

status = Body->ISetCurrentSurface ( surfaceIn )

| Input: | (LPSURFACE) surfaceIn | Pointer to a surface object; this surface might have been created using other surface creation routines, such as Modeler::CreateCylindricalSurface |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used with a set of related methods that construct a body from trimmed surfaces. This method takes a surface object created elsewhere and adds it to the temporary body object, which is acting as a placeholder for the trimmed surfaces.

Follow calls to this method with one or more calls to the trimming-curve creation methods, such as Surface::AddTrimmingLoop2. Than, trim the surface using Body::CreateTrimmedSurface. After you add all the surfaces to the body and trim appropriately, you can sew the body to create an imported SolidWorks body feature using Body::CreateBodyFromSurfaces.
