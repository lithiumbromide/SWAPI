---
title: "CreateBodyFromSurfaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateBodyFromSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.html"
---

# CreateBodyFromSurfaces Method (IBody2)

Creates a body from a list of trimmed surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBodyFromSurfaces() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.CreateBodyFromSurfaces()
```

### C#

```csharp
System.bool CreateBodyFromSurfaces()
```

### C++/CLI

```cpp
System.bool CreateBodyFromSurfaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if solid body is created

False if:

- solid body is not created
  - or -
- surface body is created

## VBA Syntax

See [Body2::CreateBodyFromSurfaces](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateBodyFromSurfaces.html).

## Examples

[Create Body Using Trimmed Surfaces (VBA)](Create_Body_using_Trimmed_Surfaces_Example_VB.htm)
[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)
[Create Imported Solid Body (C#)](Create_Imported_Solid_Body_Example_CSharp.htm)
[Create Imported Solid Body (VB.NET)](Create_Imported_Solid_Body_Example_VBNET.htm)
[Create Imported Solid Body (VBA)](Create_Imported_Solid_Body_Example_VB.htm)

## Remarks

To create a body using trimmed surfaces:

1. Create a new temporary body in a part using [IPartDoc::CreateNewBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~CreateNewBody.html).
2. Create the trimmed surfaces in the shape of the new body (for example, six square surfaces that intersect at the edges to form a cube).

  - Create a planar surface based on a root point and normal (two, three cell VARIANT arrays) using IBody2::CreatePlanarSurface(RootPoint, Normal).
  - Add a trimming loop to the planar surface using
    ISurface::AddTrimmingLoop2(Numcurves, _
    Order, _
    Dimen, _
    Periodic, _
    NumKnots, _
    NumCtrlPoints, _
    Knots, _
    CtrlPointDbls, _
    UVRange)
  - Create a trimmed surface on the body based on the trimming loop that was just created. The arguments for Surface::AddTrimmingLoop2 and their values for a square are:

    | Argument | Description |
    | --- | --- |
    | NumCurves | Number of curves that make up the loop (4 Long) |
    | Order | Orders for the spline curves ({2, 2, 2, 2} Array of Longs) |
    | Dimen | Dimension of the control points for the spline curves ({2, 2, 2, 2} Array of Longs) |
    | Periodic | Periodicity of the spline curves ({0, 0, 0, 0} Array of Longs) |
    | NumKnots | Number of Knots of the spline curves ({4, 4, 4, 4} Array of Longs) |
    | NumCtrlPoints | Number of Control points for the spline curves ({2, 2, 2, 2} Array of Longs) |
    | Knots | Describes the locations of the knots ({0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1} Array of Doubles. Each knot represented by four numbers 0, 0, 1, 1) |
    | CtrlPointDbls | Control points for the TrimmingLoop ({0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0} Array of Doubles. Describes the corners of the square) |
    | UVRange | Min and max for the U and V values ({0, 1, 0, 1} Array of Doubles) |
3. Sew the surfaces together into a new body using this method.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
