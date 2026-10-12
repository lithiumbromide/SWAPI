---
title: "ISetCurrentSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ISetCurrentSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISetCurrentSurface.html"
---

# ISetCurrentSurface Method (IBody2)

Places an existing surface into a temporary body that is under construction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetCurrentSurface( _
   ByVal SurfaceIn As Surface _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim SurfaceIn As Surface

instance.ISetCurrentSurface(SurfaceIn)
```

### C#

```csharp
void ISetCurrentSurface(
   Surface SurfaceIn
)
```

### C++/CLI

```cpp
void ISetCurrentSurface(
   Surface^ SurfaceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceIn`: Pointer to a [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html), which might have been created using other surface creation routines, such as [IModeler::ICreateCylindricalSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateCylindricalSurface2.html)

## VBA Syntax

See [Body2::ISetCurrentSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ISetCurrentSurface.html).

## Remarks

This method is used with a set of related methods that construct a body from trimmed surfaces. This method takes an ISurface object created elsewhere and adds it to the temporary body object, which acts as a placeholder for the trimmed surfaces.

Follow calls to this method with one or more calls to the trimming-curve creation methods, such as [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html). Then, trim the surface using [IBody2::CreateTrimmedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateTrimmedSurface.html). After you add all the surfaces to the body and trim appropriately, you can sew the body to create an imported SOLIDWORKS body feature using [IBody2::CreateBodyFromSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBodyFromSurfaces.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::SetCurrentSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetCurrentSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
