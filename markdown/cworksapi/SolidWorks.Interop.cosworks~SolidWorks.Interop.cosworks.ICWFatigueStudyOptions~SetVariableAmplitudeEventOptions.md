---
title: "SetVariableAmplitudeEventOptions Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "SetVariableAmplitudeEventOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetVariableAmplitudeEventOptions.html"
---

# SetVariableAmplitudeEventOptions Method (ICWFatigueStudyOptions)

Sets the options for variable amplitude fatigue events.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVariableAmplitudeEventOptions( _
   ByVal NNoOfBins As System.Integer, _
   ByVal NPercentFilterLoadCycles As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim NNoOfBins As System.Integer
Dim NPercentFilterLoadCycles As System.Integer

instance.SetVariableAmplitudeEventOptions(NNoOfBins, NPercentFilterLoadCycles)
```

### C#

```csharp
void SetVariableAmplitudeEventOptions(
   System.int NNoOfBins,
   System.int NPercentFilterLoadCycles
)
```

### C++/CLI

```cpp
void SetVariableAmplitudeEventOptions(
   System.int NNoOfBins,
   System.int NPercentFilterLoadCycles
)
```

### Parameters

- `NNoOfBins`: Number of equally spaced bins in which to distribute the loads
- `NPercentFilterLoadCycles`: Percentage of maximum load below which load cycles are filtered out

## VBA Syntax

See [CWFatigueStudyOptions::SetVariableAmplitudeEventOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~SetVariableAmplitudeEventOptions.html).

## Remarks

This method is valid only for variable amplitude fatigue studies.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::GetVariableAmplitudeEventOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetVariableAmplitudeEventOptions.html)
[ICWFatigueStudyOptions::AddFatigueEventForVariableAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForVariableAmplitude.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
