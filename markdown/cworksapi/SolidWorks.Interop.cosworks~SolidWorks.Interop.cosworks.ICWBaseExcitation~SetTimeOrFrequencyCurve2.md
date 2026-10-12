---
title: "SetTimeOrFrequencyCurve2 Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "SetTimeOrFrequencyCurve2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetTimeOrFrequencyCurve2.html"
---

# SetTimeOrFrequencyCurve2 Method (ICWBaseExcitation)

Sets the variation of base excitation with time or frequency.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeOrFrequencyCurve2( _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Boolean

value = instance.SetTimeOrFrequencyCurve2(VarCurveData, ErrorCode)
```

### C#

```csharp
System.bool SetTimeOrFrequencyCurve2(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.bool SetTimeOrFrequencyCurve2(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array (see Remarks)
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

-1 or true to use the time or frequency curve, 0 or false to not

## Remarks

Array of linear or curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where for modal time history and nonlinear dynamic studies:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = excitation value associated with time xi

and for harmonic and random vibration dynamic studies:

- n = number of xi,yi pairs
- xi = frequency value at the `ith` data point
- yi = excitation value associated with frequency xi

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
