---
title: "GetHarmonicFrequencyUnits2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetHarmonicFrequencyUnits2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUnits2.html"
---

# GetHarmonicFrequencyUnits2 Method (ICWDynamicStudyOptions)

Gets the frequency units of the harmonic dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHarmonicFrequencyUnits2( _
   ByRef NUnits As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NUnits As System.Integer
Dim value As System.Integer

value = instance.GetHarmonicFrequencyUnits2(NUnits)
```

### C#

```csharp
System.int GetHarmonicFrequencyUnits2(
   out System.int NUnits
)
```

### C++/CLI

```cpp
System.int GetHarmonicFrequencyUnits2(
   [Out] System.int NUnits
)
```

### Parameters

- `NUnits`: Units as defined by [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetHarmonicFrequencyUnits2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetHarmonicFrequencyUnits2.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUnits2.html)
[ICWDynamicStudyOptions::GetHarmonicBandwidth2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicBandwidth2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::GetHarmonicFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::GetHarmonicInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicInterpolation2.html)
[ICWDynamicStudyOptions::GetHarmonicNoOfPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicNoOfPoints2.html)
[ICWDynamicStudyOptions::SetHarmonicBandwidth2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicBandwidth2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::SetHarmonicFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::SetHarmonicInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicInterpolation2.html)
[ICWDynamicStudyOptions::SetHarmonicNoOfPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicNoOfPoints2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
