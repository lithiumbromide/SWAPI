---
title: "SetHarmonicFrequencyLowerLimit2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetHarmonicFrequencyLowerLimit2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyLowerLimit2.html"
---

# SetHarmonicFrequencyLowerLimit2 Method (ICWDynamicStudyOptions)

Sets the frequency lower limit of the harmonic dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetHarmonicFrequencyLowerLimit2( _
   ByVal DLowerLimit As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DLowerLimit As System.Double
Dim value As System.Integer

value = instance.SetHarmonicFrequencyLowerLimit2(DLowerLimit)
```

### C#

```csharp
System.int SetHarmonicFrequencyLowerLimit2(
   System.double DLowerLimit
)
```

### C++/CLI

```cpp
System.int SetHarmonicFrequencyLowerLimit2(
   System.double DLowerLimit
)
```

### Parameters

- `DLowerLimit`: Frequency lower limit

### Return Value

0 if successful, 1 if not

## VBA Syntax

See [CWDynamicStudyOptions::SetHarmonicFrequencyLowerLimit2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetHarmonicFrequencyLowerLimit2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::SetHarmonicBandwidth2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicBandwidth2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUnits2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::SetHarmonicInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicInterpolation2.html)
[ICWDynamicStudyOptions::SetHarmonicNoOfPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicNoOfPoints2.html)
[ICWDynamicStudyOptions::GetHarmonicBandwidth2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicBandwidth2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUnits2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::GetHarmonicInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicInterpolation2.html)
[ICWDynamicStudyOptions::GetHarmonicNoOfPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicNoOfPoints2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
