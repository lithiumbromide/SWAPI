---
title: "SetFrequencyOption Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetFrequencyOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyOption.html"
---

# SetFrequencyOption Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::SetFrequencyOption2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyOption2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFrequencyOption( _
   ByVal NOption As System.Integer, _
   ByVal DValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NOption As System.Integer
Dim DValue As System.Double

instance.SetFrequencyOption(NOption, DValue)
```

### C#

```csharp
void SetFrequencyOption(
   System.int NOption,
   System.double DValue
)
```

### C++/CLI

```cpp
void SetFrequencyOption(
   System.int NOption,
   System.double DValue
)
```

### Parameters

- `NOption`: Option as defined by [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html)
- `DValue`: - Number of frequencies, if NOption = [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionNumberFrequencies
  - Upper-bound frequency, if NOption = swsFrequencyStudyOption_e.swsFrequencyStudyOptionUserUpperBoundFrequency

## VBA Syntax

See [CWDynamicStudyOptions::SetFrequencyOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetFrequencyOption.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetFrequencyOption Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyOption.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
