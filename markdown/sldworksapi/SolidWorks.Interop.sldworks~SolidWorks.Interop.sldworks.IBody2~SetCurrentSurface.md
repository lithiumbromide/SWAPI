---
title: "SetCurrentSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetCurrentSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetCurrentSurface.html"
---

# SetCurrentSurface Method (IBody2)

Places an existing surface into a temporary body that is under construction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCurrentSurface( _
   ByVal SurfaceIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim SurfaceIn As System.Object

instance.SetCurrentSurface(SurfaceIn)
```

### C#

```csharp
void SetCurrentSurface(
   System.object SurfaceIn
)
```

### C++/CLI

```cpp
void SetCurrentSurface(
   System.Object^ SurfaceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceIn`: Surface, which might have been created using other surface creation routines, such as [IModeler::CreateCylindricalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateCylindricalSurface2.html)

## VBA Syntax

See [Body2::SetCurrentSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetCurrentSurface.html).

## Remarks

This method is used with a set of related methods that construct a body from trimmed surfaces. This method takes an ISurface object created elsewhere and adds it to the temporary body object, which acts as a placeholder for the trimmed surfaces.

Follow calls to this method with one or more calls to the trimming-curve creation methods, such as [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html). Then, trim the surface using [IBody2::CreateTrimmedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateTrimmedSurface.html). After you add all the surfaces to the body and trim appropriately, you can sew the body to create an imported SOLIDWORKS body feature using [IBody2::CreateBodyFromSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBodyFromSurfaces.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ISetCurrentSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISetCurrentSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
