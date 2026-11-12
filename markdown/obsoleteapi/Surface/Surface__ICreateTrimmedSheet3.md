---
title: "Surface::ICreateTrimmedSheet3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__ICreateTrimmedSheet3.htm"
---

# Surface::ICreateTrimmedSheet3

This method is obsolete and has been superseded by [Surface::CreateTrimmedSheet4](sldworksAPI.chm::/Surface/Surface__CreateTrimmedSheet4.htm).

Description

This method creates a trimmed sheet body from this surface.

Syntax (OLE Automation)

Sheet = Surface.ICreateTrimmedSheet3 ( NCurves, Curves)

Not available. See Surface::CreateTrimmedSheet.

Syntax (COM)

status = Surface->ICreateTrimmedSheet3 ( NCurves, Curves, &Sheet)

| Input: | (long) NCurves | Number of curves in the array of curves |
| --- | --- | --- |
| Input: | (LPCURVE) Curves | Array of curves that represent the boundary of the sheet |
| Output: | (LPBODY2) Sheet | Pointer to the newly created sheet body |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The array of curves represents all of the curves required to add the appropriate trimming loops to the surface. A NULL entry in the array represents the separation between loops.

The curves supplied are assumed to lie on the surface. If the curves are 2D curves, then they should be created using this surface.

If the application is creating a trimmed sheet body from an input periodical surface without trimming curves, then the curve array may be empty.
