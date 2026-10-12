---
title: "IEdgeGetFace Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "IEdgeGetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IEdgeGetFace.html"
---

# IEdgeGetFace Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::IEdgeGetFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IEdgeGetFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IEdgeGetFace( _
   ByVal EdgeInDisp As Edge _
) As Face
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface
Dim EdgeInDisp As Edge
Dim value As Face

value = instance.IEdgeGetFace(EdgeInDisp)
```

### C#

```csharp
Face IEdgeGetFace(
   Edge EdgeInDisp
)
```

### C++/CLI

```cpp
Face^ IEdgeGetFace(
   Edge^ EdgeInDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeInDisp`:

## VBA Syntax

See [MidSurface::IEdgeGetFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~IEdgeGetFace.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
