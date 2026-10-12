---
title: "IsOffset Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsOffset.html"
---

# IsOffset Method (ISurface)

Gets whether the surface is an offset surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsOffset() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsOffset()
```

### C#

```csharp
System.bool IsOffset()
```

### C++/CLI

```cpp
System.bool IsOffset();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the surface is an offset surface, false if not

## VBA Syntax

See [Surface::IsOffset](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsOffset.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.html)
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.html)
[ISurface::IGetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetOffsetSurfParams2.html)
[ISurface::GetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetOffsetSurfParams2.html)
[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
