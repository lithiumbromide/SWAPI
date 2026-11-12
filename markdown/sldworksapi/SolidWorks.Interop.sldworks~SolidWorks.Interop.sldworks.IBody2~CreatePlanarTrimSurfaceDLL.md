---
title: "CreatePlanarTrimSurfaceDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreatePlanarTrimSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarTrimSurfaceDLL.html"
---

# CreatePlanarTrimSurfaceDLL Method (IBody2)

Creates a planar trim surface for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlanarTrimSurfaceDLL( _
   ByVal Points As System.Object, _
   ByVal Normal As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Points As System.Object
Dim Normal As System.Object
Dim value As System.Boolean

value = instance.CreatePlanarTrimSurfaceDLL(Points, Normal)
```

### C#

```csharp
System.bool CreatePlanarTrimSurfaceDLL(
   System.object Points,
   System.object Normal
)
```

### C++/CLI

```cpp
System.bool CreatePlanarTrimSurfaceDLL(
   System.Object^ Points,
   System.Object^ Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Points`: Array of the points for the surface; trim curves are automatically created between each sequential vertex
- `Normal`: Array of normal vector for the surface

### Return Value

True if planar trim surface is created, false if not

## VBA Syntax

See [Body2::CreatePlanarTrimSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreatePlanarTrimSurfaceDLL.html).

## Examples

[Create Imported Solid Body (C#)](Create_Imported_Solid_Body_Example_CSharp.htm)
[Create Imported Solid Body (VB.NET)](Create_Imported_Solid_Body_Example_VBNET.htm)
[Create Imported Solid Body (VBA)](Create_Imported_Solid_Body_Example_VB.htm)

## Remarks

You can use this method instead of [IBody2:CreateTrimmedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateTrimmedSurface.html), [IBody2::ICreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreatePlanarSurface.html), and [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreatePlanarTrimSurfaceDLL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarTrimSurfaceDLL.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12
