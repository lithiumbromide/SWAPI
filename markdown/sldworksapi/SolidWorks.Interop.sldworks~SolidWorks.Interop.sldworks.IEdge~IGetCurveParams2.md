---
title: "IGetCurveParams2 Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IGetCurveParams2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.html"
---

# IGetCurveParams2 Method (IEdge)

Returns the curve parameters for this edge, including the edge and curve direction (sense).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCurveParams2() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Double

value = instance.IGetCurveParams2()
```

### C#

```csharp
System.double IGetCurveParams2()
```

### C++/CLI

```cpp
System.double IGetCurveParams2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

[Get Circular Holes in Face (C++)](Get_Circular_Holes_In_Face_Example_CPlusPlus_COM.htm)

## Remarks

Calls to this method must be preceded by a call to [IEdge::GetCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurve.html) or [IEdge::IGetCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetCurve.html) because SOLIDWORKS does not keep the underlying curve information. Edge::GetCurve generates this information so that you can extract the curve parameters.

You can use the data returned by this method to determine if a circular edge is a complete circle or an arc.

The return value is the following array of 11 doubles:

```vb
[ StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, StartUParam, EndUParam, PackDouble1, PackDouble2, PackDouble3 ]
```

where PackDouble1, PackDouble2, and PackDouble3 are each a set of two integers packed into a double. These variables hold the following pair of integers:

| PackDouble1 | Two packed integers: Unused curveType as documented in ICurve::Identity |
| --- | --- |
| PackDouble2 | Two packed integers: Unused curveTag |
| PackDouble3 | Two packed integers: Unused SenseFlag (indicates whether the curve and edge are in the same direction) |

If SenseFlag is True, then the curve and edge are in the same direction. If SenseFlag is false, then the curve and edge are in opposite directions. In this case, this method returns the start parameter (point) that corresponds to the end of the edge and the end parameter (point) that corresponds to the end of the edge.

The start parameter is always smaller than the end parameter. If the curve and edge are in opposite directions, then the start and end parameters are along the negative portion of the parameter space. For example, if the start parameter of the edge is 10 and the end parameter is 5, then the parameter range returned is -10, -5. This ensures that the start parameter is smaller than the end parameter. To correct the values for the edge, swap the two values between the start and end parameters and then negate both values so that the value of the start parameter is 5 and the end parameter is 10.

If the curve is closed and the curve starts and ends at the same point, then StartUParam and EndUParam are a period apart.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.html)
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html)
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.html)
[IEdge::IsParamReversed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsParamReversed.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
