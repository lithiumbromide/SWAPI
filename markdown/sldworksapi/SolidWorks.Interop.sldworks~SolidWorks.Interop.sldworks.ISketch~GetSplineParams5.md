---
title: "GetSplineParams5 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSplineParams5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams5.html"
---

# GetSplineParams5 Method (ISketch)

Gets the parameterization data of the specified spline in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineParams5( _
   ByVal ForceNonPeriodic As System.Boolean, _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim ForceNonPeriodic As System.Boolean
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetSplineParams5(ForceNonPeriodic, Index)
```

### C#

```csharp
System.object GetSplineParams5(
   System.bool ForceNonPeriodic,
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetSplineParams5(
   System.bool ForceNonPeriodic,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ForceNonPeriodic`: True to attempt to convert a non-periodic spline to a periodic one, false to not
- `Index`: 0-based index indicating the spline whose parameterization data to get

### Return Value

[ISplineParamData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)

## VBA Syntax

See [Sketch::GetSplineParams5](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSplineParams5.html).

## Examples

[Get Each Spline's Parameters (C#)](Get_Each_Splines_Parameters_Example_CSharp.htm)
[Get Each Spline's Parameters (VB.NET)](Get_Each_Splines_Parameters_Example_VBNET.htm)
[Get Each Spline's Parameters (VBA)](Get_Each_Splines_Parameters_Example_VB.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSplineParamsCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount.html)
[ISketch::GetSplines Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.html)
[ISketch::IGetSplines Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.html)
[ISketch::GetSplinesInterpolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.html)
[ISketch::GetSplineInterpolateCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.html)
[ISketch::GetSplineCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.html)
[ISketch::IGetSplinesInterpolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
