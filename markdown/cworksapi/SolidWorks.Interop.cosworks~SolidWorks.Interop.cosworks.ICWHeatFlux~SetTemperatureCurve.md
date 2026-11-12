---
title: "SetTemperatureCurve Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "SetTemperatureCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetTemperatureCurve.html"
---

# SetTemperatureCurve Method (ICWHeatFlux)

Obsolete. Superseded by [ICWHeatFlux::SetTemperatureCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetTemperatureCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTemperatureCurve( _
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

value = instance.SetTemperatureCurve(VarCurveData, ErrorCode)
```

### C#

```csharp
System.int SetTemperatureCurve(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.int SetTemperatureCurve(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array of temperature curve data (see **Remarks**)
- `ErrorCode`: Temperature curve error as defined in [swsTemperatureCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureCurveError_e.html)

### Return Value

1 to use temperature curve, 0 to not

## VBA Syntax

See [CWHeatFlux::SetTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~SetTemperatureCurve.html).

## Remarks

Temperature curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = temperature value at the `ith` data point
- yi = property value associated with temperature xi

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::GetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetTemperatureCurve.html)
[ICWHeatFlux::UseTemperatureCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~UseTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
