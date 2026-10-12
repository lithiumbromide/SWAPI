---
title: "Body::ICreatePlanarTrimSurfaceDLL"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__ICreatePlanarTrimSurfaceDLL.htm"
---

# Body::ICreatePlanarTrimSurfaceDLL

## Body:: ICreatePlanarTrimSurfaceDLL

This method is obsolete and has been superseded by [Body2::ICreatePlanarTrimSurfaceDLL](sldworksAPI.chm::/Body2/Body2__ICreatePlanarTrimSurfaceDLL.htm).

Description

This method creates a planar trim surface for this body.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Body::ICreatePlanarTrimSurfaceDLL(VertexCount, Points, Normal )

| Input: | (long) VertexCount | Number of vertices |
| --- | --- | --- |
| Input: | (double*) Points | Pointer to an array of doubles describing the points for the surface; SolidWorks automatically creates trim curves between each sequential vertex |
| Input: | (double*) Normal | Normal vector for the surface |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use this method instead of using [Body::CreatePlanarSurface](Body__CreatePlanarSurface.htm), [Body::CreateTrimmedSurface](Body__CreateTrimmedSurface.htm), and [Surface::AddTrimmingLoop](../Surface/Surface__AddTrimmingLoop.htm).
