---
title: "CreatePlanarSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreatePlanarSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface.html"
---

# CreatePlanarSurface Method (IModeler)

Obsolete. Superseded by [IModeler::CreatePlanarSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreatePlanarSurface2.html).

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
Dim instance As IModeler
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

See [Modeler::CreatePlanarSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreatePlanarSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
