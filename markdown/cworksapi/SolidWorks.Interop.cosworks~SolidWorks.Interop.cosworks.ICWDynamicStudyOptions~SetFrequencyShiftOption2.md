---
title: "SetFrequencyShiftOption2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetFrequencyShiftOption2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyShiftOption2.html"
---

# SetFrequencyShiftOption2 Method (ICWDynamicStudyOptions)

Sets whether to only calculate resonant frequencies that are closest to a specific frequency.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFrequencyShiftOption2( _
   ByVal BChecked As System.Boolean, _
   ByVal DFrequencyValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Boolean
Dim DFrequencyValue As System.Double
Dim value As System.Integer

value = instance.SetFrequencyShiftOption2(BChecked, DFrequencyValue)
```

### C#

```csharp
System.int SetFrequencyShiftOption2(
   System.bool BChecked,
   System.double DFrequencyValue
)
```

### C++/CLI

```cpp
System.int SetFrequencyShiftOption2(
   System.bool BChecked,
   System.double DFrequencyValue
)
```

### Parameters

- `BChecked`: True to only calculate resonant frequencies that are closest to DFrequencyValue, false to not
- `DFrequencyValue`: Frequency in Hz; valid only if BChecked = true (see **Remarks**)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetFrequencyShiftOption2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetFrequencyShiftOption2.html).

## Remarks

This method is valid only if both of the following are true:

- [ICWDynamicStudyOptions::SolverType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SolverType.html) = [swsSolverType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSolverType_e.html).swsSolverTypeDirectSparse
- [ICWDynamicStudyOptions::GetFrequencyOption2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyOption2.html) = [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html).swsFrequencyStudyOptionNumberFrequencies

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetFrequencyShiftOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyShiftOption2.html)
[ICWDynamicStudyOptions::SetFrequencyOption2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyOption2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
