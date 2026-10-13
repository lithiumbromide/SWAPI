---
title: "IGetSplineParams Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "IGetSplineParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.html"
---

# IGetSplineParams Method (ISketchBlockDefinition)

Gets all the parameters of the splines in the sketch block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSplineParams( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetSplineParams(ArraySize)
```

### C#

```csharp
System.double IGetSplineParams(
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetSplineParams(
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Size of the array needed to hold the spline parameters data

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles, containing spline parameters (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketchBlockDefinition::GetSplineParamsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetSplineParamsCount.html) before calling this method to get the value for ArraySize.

The return value is an array of doubles containing data for all the splines in the sketch block definitioni.

The first two array elements for each spline contain 4 integer values holding information that describes the rest of the data in that splines parameters:

| Spline Element | Packed Data |  |
| --- | --- | --- |
| 0 | Dim | Order |
| 1 | nCtrlPoints | Periodic |

where:

- Dim is the number of dimensions the spline is defined in
- Order is the order of the spline
- nCtrlPoints is the number of control points
- Periodic is 1 for a closed spline or 0 for an open spline

The number of knots depends on whether the spline is periodic or not:

| Periodic: | numKnots = nCtrlPoints + 1 |
| --- | --- |
| Non-Periodic: | numKnots = nCtrlPoints + Order |

The last three array elements for each spline contain 5 integer values holding style and layer information:

| Spline Element | Packed Data |  |
| --- | --- | --- |
| i | Color | lineStyle |
| i+1 | lineWidth | Layer |
| i+2 | layerOverride | Not used |

where:

- i is the index following the last Knot or [2 + numKnots + numControlPointDoubles * Dim]
- Color is the COLORREF value describing the color used for the ith spline
- lineStyle is the line style used for the ith spline. Valid values can be found in the [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration
- lineWidth is line width used for the ith spline. Valid values can be found in the [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) enumeration
- Layer is an integer index to the layer that the ith spline is on
- layerOverride is integer with bit flags set to determine which properties, if any, have been overridden or should be overridden.

Therefore, the size of the data for each spline is given by:

2 + numKnots + numControlPointDoubles * Dim + 3

The ControlPoint data (in the sketch coordinate system) follows the 2 packed data elements, the Knot points, and, finally, the last 3 packed data elements. Subsequent splines follow one another in the array.

[ packedDouble1, packedDouble2, ControlPoint1[Dimension elements], ControlPoint2[Dimension elements],... knot1, knot2,..., packedDouble3, packedDouble4, packedDouble5, ]

For information about unpacking double arrays into integer pairs, see:

- [Unpacking Double Arrays into Integer Paris in Visual Basic.NET and Visual Basic](sldworksAPIProgGuide.chm::/OVERVIEW/Unpacking_Double_Arrays_into_Integer_Pairs_in_Visual_Basic_.NET_and_Visual_Basic.htm)
- [Unpacking Double Arrays into Integer Pairs in C++](sldworksAPIProgGuide.chm::/OVERVIEW/PackedIntegersCPlusPlus.htm)
- [Unpacking Double Arrays into Integer Pairs in C#](sldworksAPIProgGuide.chm::/OVERVIEW/Unpacking_Double_Arrays_into_Integer_Pairs_in_C_.htm)

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[GetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams.html)
[ISketchBlockDefinition::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.html)
[ISketchBlockDefinition::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount.html)
[ISketchBlockDefinition::GetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.html)
[ISketchBlockDefinition::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.html)
[ISketchBlockDefinition::IGetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.html)
[ISketchBlockDefinition::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
