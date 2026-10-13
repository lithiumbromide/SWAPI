---
title: "IAddProfileArc Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IAddProfileArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileArc.html"
---

# IAddProfileArc Method (IBody)

Obsolete. Superseded by [IBody2::IAddProfileArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddProfileArc.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileArc( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal Radius As System.Double, _
   ByVal StartPoint As System.Object, _
   ByVal EndPoint As System.Object _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Center As System.Object
Dim Axis As System.Object
Dim Radius As System.Double
Dim StartPoint As System.Object
Dim EndPoint As System.Object
Dim value As Curve

value = instance.IAddProfileArc(Center, Axis, Radius, StartPoint, EndPoint)
```

### C#

```csharp
Curve IAddProfileArc(
   System.object Center,
   System.object Axis,
   System.double Radius,
   System.object StartPoint,
   System.object EndPoint
)
```

### C++/CLI

```cpp
Curve^ IAddProfileArc(
   System.Object^ Center,
   System.Object^ Axis,
   System.double Radius,
   System.Object^ StartPoint,
   System.Object^ EndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Axis`:
- `Radius`:
- `StartPoint`:
- `EndPoint`:

## VBA Syntax

See [Body::IAddProfileArc](ms-its:sldworksapivb6.chm::/sldworks~Body~IAddProfileArc.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
