---
title: "SetTimeCurve Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "SetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetTimeCurve.html"
---

# SetTimeCurve Method (ICWHeatFlux)

Obsolete. Superseded by [ICWHeatFlux::SetTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetTemperatureCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeCurve( _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Integer

value = instance.SetTimeCurve(VarCurveData, ErrorCode)
```

### C#

```csharp
System.int SetTimeCurve(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.int SetTimeCurve(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array of time curve data (see **Remarks**)
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

1 to use curve, 0 to not

## VBA Syntax

See [CWHeatFlux::SetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~SetTimeCurve.html).

## Remarks

Time curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = property value associated with time xi

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetTimeCurve.html)
[ICWHeatFlux::UseTimeCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~UseTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
