---
title: "ICreatePlanarSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreatePlanarSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreatePlanarSurface.html"
---

# ICreatePlanarSurface Method (IBody)

Obsolete. Superseded by [IBody2::ICreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePlanarSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlanarSurface( _
   ByVal VRootPoint As System.Object, _
   ByVal VNormal As System.Object _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim VRootPoint As System.Object
Dim VNormal As System.Object
Dim value As Surface

value = instance.ICreatePlanarSurface(VRootPoint, VNormal)
```

### C#

```csharp
Surface ICreatePlanarSurface(
   System.object VRootPoint,
   System.object VNormal
)
```

### C++/CLI

```cpp
Surface^ ICreatePlanarSurface(
   System.Object^ VRootPoint,
   System.Object^ VNormal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VRootPoint`:
- `VNormal`:

## VBA Syntax

See [Body::ICreatePlanarSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreatePlanarSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
