---
title: "GetFrequencyShiftOption Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetFrequencyShiftOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyShiftOption.html"
---

# GetFrequencyShiftOption Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetFrequencyShiftOption2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyShiftOption2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFrequencyShiftOption( _
   ByRef BChecked As System.Boolean, _
   ByRef DFrequencyValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Boolean
Dim DFrequencyValue As System.Double

instance.GetFrequencyShiftOption(BChecked, DFrequencyValue)
```

### C#

```csharp
void GetFrequencyShiftOption(
   out System.bool BChecked,
   out System.double DFrequencyValue
)
```

### C++/CLI

```cpp
void GetFrequencyShiftOption(
   [Out] System.bool BChecked,
   [Out] System.double DFrequencyValue
)
```

### Parameters

- `BChecked`: True to calculate only resonant frequencies that are closest to DFrequencyValue, false to not
- `DFrequencyValue`: Frequency in Hz; valid only if BChecked = true (see **Remarks**)

## VBA Syntax

See [CWDynamicStudyOptions::GetFrequencyShiftOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetFrequencyShiftOption.html).

## Remarks

This method is valid only if both of the following are true:

- [ICWDynamicStudyOptions::SolverType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SolverType.html) = swsSolverType_e.swsSolverTypeDirectSparse
- [ICWDynamicStudyOptions::GetFrequencyOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyOption.html) = swsFrequencyStudyOption_e.swsFrequencyStudyOptionNumberFrequencies

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetFrequencyShiftOption Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyShiftOption.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
