---
title: "SetHarmonicFrequencyUpperLimit2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetHarmonicFrequencyUpperLimit2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUpperLimit2.html"
---

# SetHarmonicFrequencyUpperLimit2 Method (ICWDynamicStudyOptions)

Sets the frequency upper limit of the harmonic dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetHarmonicFrequencyUpperLimit2( _
   ByVal DUpperLimit As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DUpperLimit As System.Double
Dim value As System.Integer

value = instance.SetHarmonicFrequencyUpperLimit2(DUpperLimit)
```

### C#

```csharp
System.int SetHarmonicFrequencyUpperLimit2(
   System.double DUpperLimit
)
```

### C++/CLI

```cpp
System.int SetHarmonicFrequencyUpperLimit2(
   System.double DUpperLimit
)
```

### Parameters

- `DUpperLimit`: Frequency upper limit

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetHarmonicFrequencyUpperLimit2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetHarmonicFrequencyUpperLimit2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::SetHarmonicBandwidth2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicBandwidth2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUnits2.html)
[ICWDynamicStudyOptions::SetHarmonicInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicInterpolation2.html)
[ICWDynamicStudyOptions::SetHarmonicNoOfPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicNoOfPoints2.html)
[ICWDynamicStudyOptions::GetHarmonicBandwidth2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicBandwidth2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUnits2.html)
[ICWDynamicStudyOptions::GetHarmonicInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicInterpolation2.html)
[ICWDynamicStudyOptions::GetHarmonicNoOfPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicNoOfPoints2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
