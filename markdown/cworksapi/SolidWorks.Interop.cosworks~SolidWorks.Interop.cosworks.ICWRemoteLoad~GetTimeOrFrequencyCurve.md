---
title: "GetTimeOrFrequencyCurve Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "GetTimeOrFrequencyCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetTimeOrFrequencyCurve.html"
---

# GetTimeOrFrequencyCurve Method (ICWRemoteLoad)

Gets the variation with time or frequency of this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeOrFrequencyCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim value As System.Object

value = instance.GetTimeOrFrequencyCurve()
```

### C#

```csharp
System.object GetTimeOrFrequencyCurve()
```

### C++/CLI

```cpp
System.Object^ GetTimeOrFrequencyCurve();
```

### Return Value

Array of curve data representing the variation with time or frequency of this remote load (see **Remarks**)

## VBA Syntax

See [CWRemoteLoad::GetTimeOrFrequencyCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~GetMomentOrRotationValues.html).

## Remarks

| This method gets an array of ... | If ICWStudy::AnalysisType is ... |
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
[ICWRemoteLoad::SetTimeOrFrequencyCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetTimeOrFrequencyCurve.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
