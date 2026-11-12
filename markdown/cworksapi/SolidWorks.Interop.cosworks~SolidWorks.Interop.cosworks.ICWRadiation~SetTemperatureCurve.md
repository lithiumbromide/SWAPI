---
title: "SetTemperatureCurve Method (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "SetTemperatureCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~SetTemperatureCurve.html"
---

# SetTemperatureCurve Method (ICWRadiation)

Obsolete. Superseded by [ICWRadiation::SetTemperatureCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~SetTemperatureCurve2.html).

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
Dim instance As ICWRadiation
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

## VBA Syntax

See [CWRadiation::SetTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~SetTemperatureCurve.html).

## Remarks

Temperature curve data array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = temperature value at the `ith` data point
- yi = property value associated with temperature xi

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[ICWRadiation::GetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~GetTemperatureCurve.html)
[ICWRadiation::UseTemperatureCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~UseTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
