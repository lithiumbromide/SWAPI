---
title: "SetHarmonicNoOfPoints2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetHarmonicNoOfPoints2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicNoOfPoints2.html"
---

# SetHarmonicNoOfPoints2 Method (ICWDynamicStudyOptions)

Sets the number of points for each frequency of the harmonic dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetHarmonicNoOfPoints2( _
   ByVal NPoints As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NPoints As System.Integer
Dim value As System.Integer

value = instance.SetHarmonicNoOfPoints2(NPoints)
```

### C#

```csharp
System.int SetHarmonicNoOfPoints2(
   System.int NPoints
)
```

### C++/CLI

```cpp
System.int SetHarmonicNoOfPoints2(
   System.int NPoints
)
```

### Parameters

- `NPoints`: Number of points for each frequency

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetHarmonicNoOfPoints2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetHarmonicNoOfPoints2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetHarmonicNoOfPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicNoOfPoints2.html)
[ICWDynamicStudyOptions::SetHarmonicBandwidth2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicBandwidth2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUnits2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::SetHarmonicInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicInterpolation2.html)
[ICWDynamicStudyOptions::GetHarmonicBandwidth2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicBandwidth2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUnits2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::GetHarmonicInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicInterpolation2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
