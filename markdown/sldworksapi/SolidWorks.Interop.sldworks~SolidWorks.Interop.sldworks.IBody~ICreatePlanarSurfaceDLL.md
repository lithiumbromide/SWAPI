---
title: "ICreatePlanarSurfaceDLL Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreatePlanarSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreatePlanarSurfaceDLL.html"
---

# ICreatePlanarSurfaceDLL Method (IBody)

Obsolete. Superseded by [IBody2::ICreatePlanarSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePlanarSurfaceDLL.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlanarSurfaceDLL( _
   ByRef RootPoint As System.Double, _
   ByRef Normal As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim RootPoint As System.Double
Dim Normal As System.Double
Dim value As Surface

value = instance.ICreatePlanarSurfaceDLL(RootPoint, Normal)
```

### C#

```csharp
Surface ICreatePlanarSurfaceDLL(
   ref System.double RootPoint,
   ref System.double Normal
)
```

### C++/CLI

```cpp
Surface^ ICreatePlanarSurfaceDLL(
   System.double% RootPoint,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`:
- `Normal`:

## VBA Syntax

See [Body::ICreatePlanarSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreatePlanarSurfaceDLL.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
