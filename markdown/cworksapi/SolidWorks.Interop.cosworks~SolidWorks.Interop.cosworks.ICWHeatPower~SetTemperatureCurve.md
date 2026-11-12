---
title: "SetTemperatureCurve Method (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "SetTemperatureCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetTemperatureCurve.html"
---

# SetTemperatureCurve Method (ICWHeatPower)

Obsolete. Superseded by [ICWHeatPower::SetTemperatureCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetTemperatureCurve2.html).

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
Dim instance As ICWHeatPower
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

1 to use curve, 0 to not

## VBA Syntax

See [CWHeatPower::SetTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~SetTemperatureCurve.html).

## Remarks

Temperature curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = temperature value at the `ith` data point
- yi = property value associated with temperature xi

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::GetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetTemperatureCurve.html)
[ICWHeatPower::UseTemperatureCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~UseTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
