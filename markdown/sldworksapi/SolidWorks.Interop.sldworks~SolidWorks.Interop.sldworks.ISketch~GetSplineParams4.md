---
title: "GetSplineParams4 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSplineParams4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams4.html"
---

# GetSplineParams4 Method (ISketch)

Obsolete. Superseded by [ISketch::GetSplineParams5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineParams4( _
   ByVal ForceNonPeriodic As System.Boolean _
) As SplineParamData
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim ForceNonPeriodic As System.Boolean
Dim value As SplineParamData

value = instance.GetSplineParams4(ForceNonPeriodic)
```

### C#

```csharp
SplineParamData GetSplineParams4(
   System.bool ForceNonPeriodic
)
```

### C++/CLI

```cpp
SplineParamData^ GetSplineParams4(
   System.bool ForceNonPeriodic
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ForceNonPeriodic`: True to attempt to convert a non-periodic spline to a periodic one, false to not

### Return Value

[ISplineParamData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData.html)

## VBA Syntax

See [Sketch::GetSplineParams4](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSplineParams4.html).

## Examples

[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSplineParamsCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount3.html)
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.html)
[ISketch::IGetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.html)
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.html)
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.html)
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.html)
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
