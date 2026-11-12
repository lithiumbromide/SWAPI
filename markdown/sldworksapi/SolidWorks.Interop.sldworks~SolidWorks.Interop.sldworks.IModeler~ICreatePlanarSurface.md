---
title: "ICreatePlanarSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreatePlanarSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface.html"
---

# ICreatePlanarSurface Method (IModeler)

Obsolete. Superseded by [IModeler::ICreatePlanarSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreatePlanarSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlanarSurface( _
   ByRef RootPoint As System.Double, _
   ByRef Normal As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim RootPoint As System.Double
Dim Normal As System.Double
Dim value As Surface

value = instance.ICreatePlanarSurface(RootPoint, Normal)
```

### C#

```csharp
Surface ICreatePlanarSurface(
   ref System.double RootPoint,
   ref System.double Normal
)
```

### C++/CLI

```cpp
Surface^ ICreatePlanarSurface(
   System.double% RootPoint,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`:
- `Normal`:

## VBA Syntax

See [Modeler::ICreatePlanarSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreatePlanarSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
