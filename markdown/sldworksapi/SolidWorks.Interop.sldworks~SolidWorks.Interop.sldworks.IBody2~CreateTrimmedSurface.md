---
title: "CreateTrimmedSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateTrimmedSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.html"
---

# CreateTrimmedSurface Method (IBody2)

Creates a trimmed surface from a base surface and a list of existing trimming curves.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTrimmedSurface() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.CreateTrimmedSurface()
```

### C#

```csharp
System.bool CreateTrimmedSurface()
```

### C++/CLI

```cpp
System.bool CreateTrimmedSurface();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if trimmed surface creation is successful, false if not

## VBA Syntax

See [Body2::CreateTrimmedSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateTrimmedSurface.html).

## Examples

[Create Body Using Trimmed Surfaces (VBA)](Create_Body_using_Trimmed_Surfaces_Example_VB.htm)
[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

## Remarks

Before you call this method, you must call one of the base-surface creation methods (such as [IBody2::CreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreatePlanarSurface.html) or [IBody2::ICreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePlanarSurface.html)) and the trimming-curve creation method [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html) or [ISurface::IAddTrimmingLoops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IAddTrimmingLoop2.html).

This method serves as the final call in a set of related functions that are designed to construct a trimmed surface from a base surface (possibly infinite) and a set of trimming curves.

If you want to construct a solid body from trimmed surfaces, call [IPartDoc::CreateNewBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~CreateNewBody.html) or [IPartDoc::ICreateNewBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateNewBody2.html) first, which arranges for a place-holder for this trimmed surface.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
