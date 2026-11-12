---
title: "SetTimeCurve Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "SetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetTimeCurve.html"
---

# SetTimeCurve Method (ICWPressure)

Obsolete. Superseded by [ICWPressure::SetTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeCurve( _
   ByVal VarCurveDate As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim VarCurveDate As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Integer

value = instance.SetTimeCurve(VarCurveDate, ErrorCode)
```

### C#

```csharp
System.int SetTimeCurve(
   System.object VarCurveDate,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.int SetTimeCurve(
   System.Object^ VarCurveDate,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveDate`: Array of time curve data (see **Remarks**)
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

1 to use time curve, 0 to not

## VBA Syntax

See [CWPressure::SetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~SetTimeCurve.html).

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
[ICWPressure::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
