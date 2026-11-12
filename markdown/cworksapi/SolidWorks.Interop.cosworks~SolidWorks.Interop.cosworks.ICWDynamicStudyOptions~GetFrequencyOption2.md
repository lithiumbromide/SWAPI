---
title: "GetFrequencyOption2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetFrequencyOption2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyOption2.html"
---

# GetFrequencyOption2 Method (ICWDynamicStudyOptions)

Gets the number or upper bound of resonant frequencies calculated in the dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrequencyOption2( _
   ByRef NOption As System.Integer, _
   ByRef DValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NOption As System.Integer
Dim DValue As System.Double
Dim value As System.Integer

value = instance.GetFrequencyOption2(NOption, DValue)
```

### C#

```csharp
System.int GetFrequencyOption2(
   out System.int NOption,
   out System.double DValue
)
```

### C++/CLI

```cpp
System.int GetFrequencyOption2(
   [Out] System.int NOption,
   [Out] System.double DValue
)
```

### Parameters

- `NOption`: Option as defined by [swsFrequencyStudyOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyStudyOption_e.html)
- `DValue`: - Number of frequencies, if NOption = swsFrequencyStudyOption_e.swsFrequencyStudyOptionNumberFrequencies

  - Upper-bound frequency, if NOption = swsFrequencyStudyOption_e.swsFrequencyStudyOptionUserUpperBoundFrequency

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetFrequencyOption2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetFrequencyOption2.html)

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetFrequencyOption2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyOption2.html)
[ICWDynamicStudyOptions::GetFrequencyShiftOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetFrequencyShiftOption2.html)
[ICWDynamicStudyOptions::SetFrequencyShiftOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetFrequencyShiftOption2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
