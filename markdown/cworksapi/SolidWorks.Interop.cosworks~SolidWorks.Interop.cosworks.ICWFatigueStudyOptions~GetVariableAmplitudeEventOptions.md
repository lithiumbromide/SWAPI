---
title: "GetVariableAmplitudeEventOptions Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "GetVariableAmplitudeEventOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetVariableAmplitudeEventOptions.html"
---

# GetVariableAmplitudeEventOptions Method (ICWFatigueStudyOptions)

Gets the options for variable amplitude fatigue events.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetVariableAmplitudeEventOptions( _
   ByRef NNoOfBins As System.Integer, _
   ByRef NPercentFilterLoadCycles As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim NNoOfBins As System.Integer
Dim NPercentFilterLoadCycles As System.Integer

instance.GetVariableAmplitudeEventOptions(NNoOfBins, NPercentFilterLoadCycles)
```

### C#

```csharp
void GetVariableAmplitudeEventOptions(
   out System.int NNoOfBins,
   out System.int NPercentFilterLoadCycles
)
```

### C++/CLI

```cpp
void GetVariableAmplitudeEventOptions(
   [Out] System.int NNoOfBins,
   [Out] System.int NPercentFilterLoadCycles
)
```

### Parameters

- `NNoOfBins`: Number of equally spaced bins in which to distribute the loads
- `NPercentFilterLoadCycles`: Percentage of maximum load below which load cycles are filtered out

## VBA Syntax

See [CWFatigueStudyOptions::GetVariableAmplitudeEventOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~GetVariableAmplitudeEventOptions.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## Remarks

This method is valid only for variable amplitude fatigue studies.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::SetVariableAmplitudeEventOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetVariableAmplitudeEventOptions.html)
[ICWFatigueStudyOptions::AddFatigueEventForVariableAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForVariableAmplitude.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
