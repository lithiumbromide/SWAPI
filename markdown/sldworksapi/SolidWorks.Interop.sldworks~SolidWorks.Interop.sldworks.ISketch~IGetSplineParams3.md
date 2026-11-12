---
title: "IGetSplineParams3 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetSplineParams3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams3.html"
---

# IGetSplineParams3 Method (ISketch)

Obsolete. Superseded by [ISketch::GetSplineParams4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSplineParams3( _
   ByVal ForceNonPeriodic As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim ForceNonPeriodic As System.Boolean
Dim value As System.Double

value = instance.IGetSplineParams3(ForceNonPeriodic)
```

### C#

```csharp
System.double IGetSplineParams3(
   System.bool ForceNonPeriodic
)
```

### C++/CLI

```cpp
System.double IGetSplineParams3(
   System.bool ForceNonPeriodic
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ForceNonPeriodic`: True to attempt to convert all non-periodic splines to periodic, false to not

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [ISketch::GetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchSegments.html) or [ISketch::IEnumSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IEnumSketchSegments.html) for access to individual [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) and [ISketchSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline.html) objects.

The return value is an array of doubles containing data for all the splines in the sketch:

[ packedDouble1, packedDouble2, ControlPoint1[Dimension elements], ControlPoint2[Dimension elements],... knot1, knot2,..., packedDouble3, packedDouble4, packedDouble5, ]

`packedDouble1 and packedDouble2`

The first two array elements for each spline contain four integer values holding information that describes the rest of the data in that spline's parameters:

| Spline Element | Packed Data |  |
| --- | --- | --- |
| 0 | Dim | Order |
| 1 | nCtrlPoints | Periodic |

where:

- Dim is the number of dimensions in which the spline is defined
- Order is the order of the spline
- nCtrlPoints is the number of control points
- Periodic is 1 for a closed spline or 0 for an open spline

`ControlPoint#`

The ControlPoint data (in the sketch coordinate system) follows the two packed data elements.

`knots#`

The number of knots depends on whether the spline is periodic or not:

| Periodic: | numKnots = nCtrlPoints + 1 |
| --- | --- |
| Non-Periodic: | numKnots = nCtrlPoints + Order |

**`packedDouble3, packedDouble4, and packedDouble5`**

The last three array elements for each spline contain five integer values holding style and layer information:

| Spline Element | Packed Data |  |
| --- | --- | --- |
| i | Color | lineStyle |
| i+1 | lineWidth | Layer |
| i+2 | layerOverride | Not used |

where:

- i is the index following the last Knot or [2 + numKnots + numControlPointDoubles * Dim]
- Color is the COLORREF value describing the color used for the `ith` spline
- lineStyle is the line style used for the ith spline. Valid values can be found in the [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration
- lineWidth is line width used for the ith spline. Valid values can be found in the [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) enumeration
- Layer is an integer index to the layer that the ith spline is on
- layerOverride is integer with bit flags set to determine which properties, if any, have been overridden or should be overridden.

Therefore, the size of the data for each spline is given by:

2 + numKnots + numControlPointDoubles * Dim + 3

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.html)
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.html)
[ISketch::GetSplineParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams3.html)
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.html)
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.html)
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.html)
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
