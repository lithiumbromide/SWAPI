---
title: "IAddProfileArc Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IAddProfileArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArc.html"
---

# IAddProfileArc Method (IBody2)

Creates an arc profile curve and returns a pointer to that curve.

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
Dim instance As IBody2
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

- `Center`: **Array of 3 doubles (x,y,z)**
- `Axis`: **Array of 3 doubles (x,y,z)**
- `Radius`: Arc radius
- `StartPoint`: **Array of 3 doubles (x,y,z)**
- `EndPoint`: **Array of 3 doubles (x,y,z)**

### Return Value

[ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::IAddProfileArc](ms-its:sldworksapivb6.chm::/sldworks~Body2~IAddProfileArc.html).

## Examples

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

## Remarks

This method always creates a full circle.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::AddProfileArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileArc.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
