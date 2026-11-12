---
title: "SetTimeCurve Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetTimeCurve.html"
---

# SetTimeCurve Method (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::SetTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetTimeCurve2.html).

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
Dim instance As ICWNonLinearStudyOptions
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
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

1 to use the time curve, 0 to not

## VBA Syntax

See [CWNonLinearStudyOptions::SetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SetTimeCurve.html).

## Remarks

Array of time curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of pairs of data points
- xi = time value at the `ith` data point
- yi = property value associated with time xi

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2010 SP3
