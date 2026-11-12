---
title: "AddProfileArc Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "AddProfileArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileArc.html"
---

# AddProfileArc Method (IBody2)

Creates an arc profile curve and returns a pointer to that curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddProfileArc( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal Radius As System.Double, _
   ByVal StartPoint As System.Object, _
   ByVal EndPoint As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Center As System.Object
Dim Axis As System.Object
Dim Radius As System.Double
Dim StartPoint As System.Object
Dim EndPoint As System.Object
Dim value As System.Object

value = instance.AddProfileArc(Center, Axis, Radius, StartPoint, EndPoint)
```

### C#

```csharp
System.object AddProfileArc(
   System.object Center,
   System.object Axis,
   System.double Radius,
   System.object StartPoint,
   System.object EndPoint
)
```

### C++/CLI

```cpp
System.Object^ AddProfileArc(
   System.Object^ Center,
   System.Object^ Axis,
   System.double Radius,
   System.Object^ StartPoint,
   System.Object^ EndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`: Array of 3 doubles (x,y,z)
- `Axis`: Array of 3 doubles (x,y,z)
- `Radius`: Arc radius
- `StartPoint`: Array of 3 doubles (x,y,z)
- `EndPoint`: Array of 3 doubles (x,y,z)

### Return Value

Object for the curve

## VBA Syntax

See [Body2::AddProfileArc](ms-its:sldworksapivb6.chm::/sldworks~Body2~AddProfileArc.html).

## Remarks

This method always creates a full circle.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IAddProfileArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArc.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
