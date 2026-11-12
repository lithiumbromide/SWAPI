---
title: "IAddProfileLine Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IAddProfileLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileLine.html"
---

# IAddProfileLine Method (IBody)

Obsolete. Superseded by [IBody2::IAddProfileLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddProfileLine.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As Curve

value = instance.IAddProfileLine(RootPoint, Direction)
```

### C#

```csharp
Curve IAddProfileLine(
   System.object RootPoint,
   System.object Direction
)
```

### C++/CLI

```cpp
Curve^ IAddProfileLine(
   System.Object^ RootPoint,
   System.Object^ Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`:
- `Direction`:

## VBA Syntax

See [Body::IAddProfileLine](ms-its:sldworksapivb6.chm::/sldworks~Body~IAddProfileLine.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
