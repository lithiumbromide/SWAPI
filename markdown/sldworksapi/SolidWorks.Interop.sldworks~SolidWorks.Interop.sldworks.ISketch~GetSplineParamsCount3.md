---
title: "GetSplineParamsCount3 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSplineParamsCount3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount3.html"
---

# GetSplineParamsCount3 Method (ISketch)

Gets the number of splines in the sketch and the size of array required to hold the data for them.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineParamsCount3( _
   ByVal ForceNonPeriodic As System.Boolean, _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim ForceNonPeriodic As System.Boolean
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetSplineParamsCount3(ForceNonPeriodic, Size)
```

### C#

```csharp
System.int GetSplineParamsCount3(
   System.bool ForceNonPeriodic,
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetSplineParamsCount3(
   System.bool ForceNonPeriodic,
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ForceNonPeriodic`: True to attempt to convert all non-periodic splines to periodic, false to not
- `Size`: Size of array required for a call to [ISketch::IGetSplineParams3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSplineParams3.html)

### Return Value

Number of [splines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSplineParams3.html)

## VBA Syntax

See [Sketch::GetSplineParamsCount3](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSplineParamsCount3.html).

## Examples

[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.html)
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.html)
[ISketch::IGetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.html)
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.html)
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.html)
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.html)
[ISketch::GetSplineParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams3.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
