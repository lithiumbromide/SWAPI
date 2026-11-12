---
title: "ICreateSheetFromSurface2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateSheetFromSurface2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.html"
---

# ICreateSheetFromSurface2 Method (IModeler)

Creates a sheet (surface) body from a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSheetFromSurface2( _
   ByVal SurfaceIn As Surface, _
   ByRef UvRange As System.Double _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim SurfaceIn As Surface
Dim UvRange As System.Double
Dim value As Body2

value = instance.ICreateSheetFromSurface2(SurfaceIn, UvRange)
```

### C#

```csharp
Body2 ICreateSheetFromSurface2(
   Surface SurfaceIn,
   ref System.double UvRange
)
```

### C++/CLI

```cpp
Body2^ ICreateSheetFromSurface2(
   Surface^ SurfaceIn,
   System.double% UvRange
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceIn`: [Surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) from which you want to create this sheet body
- `UvRange`: Array of UV values for this surface

### Return Value

Newly created [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::ICreateSheetFromSurface2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateSheetFromSurface2.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateSheetFromSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface.html)
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.html)
[ISurface::CreateTrimmedSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet.html)
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
