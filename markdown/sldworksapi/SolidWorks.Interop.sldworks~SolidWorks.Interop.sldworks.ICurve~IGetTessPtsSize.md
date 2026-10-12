---
title: "IGetTessPtsSize Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetTessPtsSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetTessPtsSize.html"
---

# IGetTessPtsSize Method (ICurve)

Gets the size of the array required by [ICurve::IGetTessPts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetTessPts.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessPtsSize( _
   ByVal ChordTolerance As System.Double, _
   ByVal LengthTolerance As System.Double, _
   ByRef StartPoint As System.Double, _
   ByRef EndPoint As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim ChordTolerance As System.Double
Dim LengthTolerance As System.Double
Dim StartPoint As System.Double
Dim EndPoint As System.Double
Dim value As System.Integer

value = instance.IGetTessPtsSize(ChordTolerance, LengthTolerance, StartPoint, EndPoint)
```

### C#

```csharp
System.int IGetTessPtsSize(
   System.double ChordTolerance,
   System.double LengthTolerance,
   ref System.double StartPoint,
   ref System.double EndPoint
)
```

### C++/CLI

```cpp
System.int IGetTessPtsSize(
   System.double ChordTolerance,
   System.double LengthTolerance,
   System.double% StartPoint,
   System.double% EndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ChordTolerance`: Chord tolerance to be used in tessellation (meters); this is the maximum permitted
  distance from a cord to the curve between the cord endpoints
- `LengthTolerance`: Length tolerance to be used to filter out very short segments (meters); tessellated
  segments shorter than this value are not returned
- `StartPoint`: Pointer to an array containing the start point of the curve
- `EndPoint`: Pointer to an array containing the end point of the curve

### Return Value

Number of doubles returned when [ICurve::IGetTessPts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetTessPts.html) is called

## VBA Syntax

See [Curve::IGetTessPtsSize](ms-its:sldworksapivb6.chm::/sldworks~Curve~IGetTessPtsSize.html).

## Remarks

To get the actual tessellation points, use [ICurve::IGetTessPts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetTessPts.html). Arguments passed to ICurve::IGetTessPts must match the arguments passed to this method.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetTessPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetTessPts.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
