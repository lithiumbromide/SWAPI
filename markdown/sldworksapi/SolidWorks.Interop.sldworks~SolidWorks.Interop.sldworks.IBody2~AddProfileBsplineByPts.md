---
title: "AddProfileBsplineByPts Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "AddProfileBsplineByPts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBsplineByPts.html"
---

# AddProfileBsplineByPts Method (IBody2)

Adds a profile B-spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddProfileBsplineByPts( _
   ByVal NumPoints As System.Integer, _
   ByVal PointArray As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumPoints As System.Integer
Dim PointArray As System.Object
Dim value As System.Object

value = instance.AddProfileBsplineByPts(NumPoints, PointArray)
```

### C#

```csharp
System.object AddProfileBsplineByPts(
   System.int NumPoints,
   System.object PointArray
)
```

### C++/CLI

```cpp
System.Object^ AddProfileBsplineByPts(
   System.int NumPoints,
   System.Object^ PointArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumPoints`: Number of B-spline points
- `PointArray`: 0-based array of 3 * NumPoints doubles

### Return Value

Pointer to the profile B-spline, [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::AddProfileBsplineByPts](ms-its:sldworksapivb6.chm::/sldworks~Body2~AddProfileBsplineByPts.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IAddProfileBsplineByPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineByPts.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
