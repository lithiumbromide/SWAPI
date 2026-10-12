---
title: "IAddProfileArcDLL Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IAddProfileArcDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileArcDLL.html"
---

# IAddProfileArcDLL Method (IBody)

Obsolete. Superseded by [IBody2::IAddProfileArcDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddProfileArcDLL.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileArcDLL( _
   ByRef Center As System.Double, _
   ByRef Axis As System.Double, _
   ByVal Radius As System.Double, _
   ByRef StartPoint As System.Double, _
   ByRef EndPoint As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Center As System.Double
Dim Axis As System.Double
Dim Radius As System.Double
Dim StartPoint As System.Double
Dim EndPoint As System.Double
Dim value As Curve

value = instance.IAddProfileArcDLL(Center, Axis, Radius, StartPoint, EndPoint)
```

### C#

```csharp
Curve IAddProfileArcDLL(
   ref System.double Center,
   ref System.double Axis,
   System.double Radius,
   ref System.double StartPoint,
   ref System.double EndPoint
)
```

### C++/CLI

```cpp
Curve^ IAddProfileArcDLL(
   System.double% Center,
   System.double% Axis,
   System.double Radius,
   System.double% StartPoint,
   System.double% EndPoint
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

See [Body::IAddProfileArcDLL](ms-its:sldworksapivb6.chm::/sldworks~Body~IAddProfileArcDLL.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
