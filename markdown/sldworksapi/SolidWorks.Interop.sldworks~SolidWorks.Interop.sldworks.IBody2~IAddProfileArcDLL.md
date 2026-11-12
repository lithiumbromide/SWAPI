---
title: "IAddProfileArcDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IAddProfileArcDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArcDLL.html"
---

# IAddProfileArcDLL Method (IBody2)

Adds a profile arc.

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
Dim instance As IBody2
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

- `Center`: Pointer to an array of 3 doubles (x,y,z)
- `Axis`: Pointer to an array of 3 doubles (x,y,z)
- `Radius`: Radius of the arc
- `StartPoint`: Pointer to an array of 3 doubles (x,y,z)
- `EndPoint`: Pointer to an array of 3 doubles (x,y,z)

### Return Value

Pointer to the arc profile [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::IAddProfileArcDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~IAddProfileArcDLL.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision 10.0
