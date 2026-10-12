---
title: "SetFrequencyOption2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetFrequencyOption2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyOption2.html"
---

# SetFrequencyOption2 Method (ICWDynamicStudyOptions)

Sets the number or upper bound of resonant frequencies calculated in the dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFrequencyOption2( _
   ByVal NOption As System.Integer, _
   ByVal DValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NOption As System.Integer
Dim DValue As System.Double
Dim value As System.Integer

value = instance.SetFrequencyOption2(NOption, DValue)
```

### C#

```csharp
System.int SetFrequencyOption2(
   System.int NOption,
   System.double DValue
)
```

### C++/CLI

```cpp
System.int SetFrequencyOption2(
   System.int NOption,
   System.double DValue
)
```

### Parameters

- `NOption`: Option as defined by [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html)
- `DValue`: - Number of frequencies, if NOption = swsFrequencyStudyOption_e.swsFrequencyStudyOptionNumberFrequencies
  - Upper-bound frequency, if NOption = swsFrequencyStudyOption_e.swsFrequencyStudyOptionUserUpperBoundFrequency

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetFrequencyOption2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetFrequencyOption2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetFrequencyOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyOption2.html)
[ICWDynamicStudyOptions::SetFrequencyShiftOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyShiftOption2.html)
[ICWDynamicStudyOptions::GetFrequencyShiftOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyShiftOption2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
