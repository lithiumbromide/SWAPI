---
title: "CreatePlanarSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreatePlanarSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreatePlanarSurface.html"
---

# CreatePlanarSurface Method (IBody)

Obsolete. Superseded by [IBody2::CreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreatePlanarSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlanarSurface( _
   ByVal VRootPoint As System.Object, _
   ByVal VNormal As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim VRootPoint As System.Object
Dim VNormal As System.Object
Dim value As System.Object

value = instance.CreatePlanarSurface(VRootPoint, VNormal)
```

### C#

```csharp
System.object CreatePlanarSurface(
   System.object VRootPoint,
   System.object VNormal
)
```

### C++/CLI

```cpp
System.Object^ CreatePlanarSurface(
   System.Object^ VRootPoint,
   System.Object^ VNormal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VRootPoint`:
- `VNormal`:

## VBA Syntax

See [Body::CreatePlanarSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~CreatePlanarSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
