---
title: "GetFrequencyOption Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetFrequencyOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyOption.html"
---

# GetFrequencyOption Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetFrequencyOption2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyOption2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFrequencyOption( _
   ByRef NOption As System.Integer, _
   ByRef DValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NOption As System.Integer
Dim DValue As System.Double

instance.GetFrequencyOption(NOption, DValue)
```

### C#

```csharp
void GetFrequencyOption(
   out System.int NOption,
   out System.double DValue
)
```

### C++/CLI

```cpp
void GetFrequencyOption(
   [Out] System.int NOption,
   [Out] System.double DValue
)
```

### Parameters

- `NOption`: Option as defined by [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html)
- `DValue`: - Number of frequencies, if NOption = [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionNumberFrequencies
  - Upper-bound frequency, if NOption = swsFrequencyStudyOption_e.swsFrequencyStudyOptionUserUpperBoundFrequency

## VBA Syntax

See [CWDynamicStudyOptions::GetFrequencyOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetFrequencyOption.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetFrequencyOption Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyOption.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
