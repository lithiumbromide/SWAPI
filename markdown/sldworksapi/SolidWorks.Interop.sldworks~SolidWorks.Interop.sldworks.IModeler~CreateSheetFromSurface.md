---
title: "CreateSheetFromSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateSheetFromSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface.html"
---

# CreateSheetFromSurface Method (IModeler)

Creates a sheet (surface) body from a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSheetFromSurface( _
   ByVal SurfaceIn As System.Object, _
   ByVal UvRange As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim SurfaceIn As System.Object
Dim UvRange As System.Object
Dim value As System.Object

value = instance.CreateSheetFromSurface(SurfaceIn, UvRange)
```

### C#

```csharp
System.object CreateSheetFromSurface(
   System.object SurfaceIn,
   System.object UvRange
)
```

### C++/CLI

```cpp
System.Object^ CreateSheetFromSurface(
   System.Object^ SurfaceIn,
   System.Object^ UvRange
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceIn`: [Surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) from which you want to create this sheet body
- `UvRange`: Array of UV values for this surface

### Return Value

Newly created [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::CreateSheetFromSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateSheetFromSurface.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.html)
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.html)
[IModeler::ICreateSheetFromSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.html)
[ISurface::CreateTrimmedSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
