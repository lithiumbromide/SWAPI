---
title: "IAddProfileLineDLL Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IAddProfileLineDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileLineDLL.html"
---

# IAddProfileLineDLL Method (IBody)

Obsolete. Superseded by [IBody2::IAddProfileLineDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddProfileLineDLL.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileLineDLL( _
   ByRef RootPoint As System.Double, _
   ByRef Direction As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim RootPoint As System.Double
Dim Direction As System.Double
Dim value As Curve

value = instance.IAddProfileLineDLL(RootPoint, Direction)
```

### C#

```csharp
Curve IAddProfileLineDLL(
   ref System.double RootPoint,
   ref System.double Direction
)
```

### C++/CLI

```cpp
Curve^ IAddProfileLineDLL(
   System.double% RootPoint,
   System.double% Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`:
- `Direction`:

## VBA Syntax

See [Body::IAddProfileLineDLL](ms-its:sldworksapivb6.chm::/sldworks~Body~IAddProfileLineDLL.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
