---
title: "SetTimeCurve2 Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "SetTimeCurve2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetTimeCurve2.html"
---

# SetTimeCurve2 Method (ICWPressure)

Sets the time curve data for this time-dependent pressure in a dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeCurve2( _
   ByVal VarCurveDate As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim VarCurveDate As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Boolean

value = instance.SetTimeCurve2(VarCurveDate, ErrorCode)
```

### C#

```csharp
System.bool SetTimeCurve2(
   System.object VarCurveDate,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.bool SetTimeCurve2(
   System.Object^ VarCurveDate,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveDate`: Array of time curve data (see **Remarks**)
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

-1 or true to use time curve, 0 or false to not

## Remarks

Array of time curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = property value associated with time xi

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
