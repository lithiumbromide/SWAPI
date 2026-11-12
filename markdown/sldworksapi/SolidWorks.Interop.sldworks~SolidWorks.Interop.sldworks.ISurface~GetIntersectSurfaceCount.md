---
title: "GetIntersectSurfaceCount Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetIntersectSurfaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectSurfaceCount.html"
---

# GetIntersectSurfaceCount Method (ISurface)

Gets the number of curves for a surface-surface intersection.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectSurfaceCount( _
   ByVal OtherSurface As Surface _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim OtherSurface As Surface
Dim value As System.Integer

value = instance.GetIntersectSurfaceCount(OtherSurface)
```

### C#

```csharp
System.int GetIntersectSurfaceCount(
   Surface OtherSurface
)
```

### C++/CLI

```cpp
System.int GetIntersectSurfaceCount(
   Surface^ OtherSurface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherSurface`: Other [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

### Return Value

Number of curves

## VBA Syntax

See [Surface::GetIntersectSurfaceCount](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetIntersectSurfaceCount.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IntersectSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectSurface.html)
[ISurface::IIntersectSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
