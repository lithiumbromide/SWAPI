---
title: "SetFrequencyShiftOption Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetFrequencyShiftOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyShiftOption.html"
---

# SetFrequencyShiftOption Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::SetFrequencyShiftOption2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyShiftOption2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFrequencyShiftOption( _
   ByVal BChecked As System.Boolean, _
   ByVal DFrequencyValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Boolean
Dim DFrequencyValue As System.Double

instance.SetFrequencyShiftOption(BChecked, DFrequencyValue)
```

### C#

```csharp
void SetFrequencyShiftOption(
   System.bool BChecked,
   System.double DFrequencyValue
)
```

### C++/CLI

```cpp
void SetFrequencyShiftOption(
   System.bool BChecked,
   System.double DFrequencyValue
)
```

### Parameters

- `BChecked`: True to only calculate resonant frequencies that are closest to DFrequencyValue, false to not
- `DFrequencyValue`: Frequency in Hz; valid only if BChecked = true (see **Remarks**)

## VBA Syntax

See [CWDynamicStudyOptions::SetFrequencyShiftOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetFrequencyShiftOption.html).

## Remarks

This method is valid only if both of the following are true:

- [ICWDynamicStudyOptions::SolverType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SolverType.html) = [swsSolverType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSolverType_e.html).swsSolverTypeDirectSparse
- [ICWDynamicStudyOptions::GetFrequencyOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyOption.html) = [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionNumberFrequencies

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetFrequencyShiftOption Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyShiftOption.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
