---
title: "IAddProfileBspline Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IAddProfileBspline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileBspline.html"
---

# IAddProfileBspline Method (IBody)

Obsolete. Superseded by [IBody2::IAddProfileBspline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddProfileBspline.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileBspline( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As Curve

value = instance.IAddProfileBspline(Props, Knots, CtrlPtCoords)
```

### C#

```csharp
Curve IAddProfileBspline(
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
Curve^ IAddProfileBspline(
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Props`:
- `Knots`:
- `CtrlPtCoords`:

## VBA Syntax

See [Body::IAddProfileBspline](ms-its:sldworksapivb6.chm::/sldworks~Body~IAddProfileBspline.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
