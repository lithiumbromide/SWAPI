---
title: "SetTimeOrFrequencyCurve Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "SetTimeOrFrequencyCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetTimeOrFrequencyCurve.html"
---

# SetTimeOrFrequencyCurve Method (ICWBaseExcitation)

Obsolete. Superseded by [ICWBaseExcitation::SetTimeOrFrequencyCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetTimeOrFrequencyCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeOrFrequencyCurve( _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Integer

value = instance.SetTimeOrFrequencyCurve(VarCurveData, ErrorCode)
```

### C#

```csharp
System.int SetTimeOrFrequencyCurve(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.int SetTimeOrFrequencyCurve(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array (see Remarks)
- `ErrorCode`: 0 if successful, 1 if not

### Return Value

1 to use the time or frequency curve, 0 to not

## VBA Syntax

See [CWBaseExcitation::SetTimeOrFrequencyCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~SetTimeOrFrequencyCurve.html).

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
[ICWBaseExcitation::GetTimeOrFrequencyCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetTimeOrFrequencyCurve.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
