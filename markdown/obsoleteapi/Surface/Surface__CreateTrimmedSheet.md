---
title: "Surface::CreateTrimmedSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__CreateTrimmedSheet.htm"
---

# Surface::CreateTrimmedSheet

This method is obsolete and has been superseded by [Surface::CreateTrimmedSheet4](sldworksAPI.chm::/Surface/Surface__CreateTrimmedSheet4.htm).

Description

This method creates a trimmed sheet body from this surface.

Syntax (OLE Automation)

retval = Surface.CreateTrimmedSheet ( curves )

| Input: | (VARIANT) curves | Array of curve objects that represent the boundary of the sheet |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created sheet body |

Syntax (COM)

This method is obsolete and has been superseded by ISurface::ICreateTrimmedSheet3.

status = Surface->ICreateTrimmedSheet ( nCurves, curves, &sheet )

| Input: | (long) nCurves | Number of curves in the array of curves |
| --- | --- | --- |
| Input: | (LPCURVE*) curves | Array of curve pointers that represent the boundary of the sheet |
| Output: | (LPBODY) sheet | Pointer to the newly created sheet body |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The array of curves represents all of the curves required to add the appropriate trimming loops to the surface. A NULL entry in the array represents the separation between loops.

The curves supplied are assumed to lie on the surface. If the curves are 2D curves, then they should be created using this surface.

If your application is creating a trimmed sheet body from an input periodical surface without trimming curves, then the curve array may be empty.

If your application uses Surface::CreateTrimmedSheet, then your application must also use Curve::CreateTrimmedCurve2 for the curves created by Modeler::CreateArc and Modeler::CreateLine.
