---
title: "SetTimeOrFrequencyCurve Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetTimeOrFrequencyCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetTimeOrFrequencyCurve.html"
---

# SetTimeOrFrequencyCurve Method (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::SetTimeOrFrequencyCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetTimeOrFrequencyCurve2.html).

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
Dim instance As ICWRemoteLoad
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

- `VarCurveData`: Array of curve data representing the variation with time or frequency of this remote load (see **Remarks**)
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

Error code as defined in [swsRemoteLoadEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRemoteLoadEndEditError_e.html)

## VBA Syntax

See [CWRemoteLoad::SetTimeOrFrequencyCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~SetMomentOrRotationValues.html).

## Remarks

| This method sets an array of ... | If ICWStudy::AnalysisType is ... |
| --- | --- |
| Time curve data | swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear |
| Frequency curve data | swsAnalysisStudyType_e.swsAnalysisStudyTypeDynamic (Harmonic or Random Vibration dynamic study sub-options only) |

Array of time or frequency curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time or frequency value at the `ith` data point
- yi = property value associated with time or frequency xi

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::GetTimeOrFrequencyCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetTimeOrFrequencyCurve.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
