---
title: "IAddProfileBsplineByPts Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IAddProfileBsplineByPts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineByPts.html"
---

# IAddProfileBsplineByPts Method (IBody2)

Adds a profile B-spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileBsplineByPts( _
   ByVal NumPoints As System.Integer, _
   ByRef PointArray As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumPoints As System.Integer
Dim PointArray As System.Double
Dim value As Curve

value = instance.IAddProfileBsplineByPts(NumPoints, PointArray)
```

### C#

```csharp
Curve IAddProfileBsplineByPts(
   System.int NumPoints,
   ref System.double PointArray
)
```

### C++/CLI

```cpp
Curve^ IAddProfileBsplineByPts(
   System.int NumPoints,
   System.double% PointArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumPoints`: Number of B-spline points
- `PointArray`: 0-based array of 3 * NumPoints doubles

### Return Value

Pointer to the profile B-spline, [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::IAddProfileBsplineByPts](ms-its:sldworksapivb6.chm::/sldworks~Body2~IAddProfileBsplineByPts.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::AddProfileBsplineByPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBsplineByPts.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
