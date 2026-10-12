---
title: "SetTemperatureCurve2 Method (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "SetTemperatureCurve2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~SetTemperatureCurve2.html"
---

# SetTemperatureCurve2 Method (ICWRadiation)

Sets the temperature curve data for this radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTemperatureCurve2( _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Boolean

value = instance.SetTemperatureCurve2(VarCurveData, ErrorCode)
```

### C#

```csharp
System.bool SetTemperatureCurve2(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.bool SetTemperatureCurve2(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array of temperature curve data (see **Remarks**)
- `ErrorCode`: Temperature curve error as defined in [swsTemperatureCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureCurveError_e.html)

### Return Value

-1 or true to use curve, 0 or false to not

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

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
