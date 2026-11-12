---
title: "SetExtraFrequenciesUnit Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetExtraFrequenciesUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesUnit.html"
---

# SetExtraFrequenciesUnit Method (ICWDynamicStudyOptions)

Sets the units of extra frequencies.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExtraFrequenciesUnit( _
   ByVal NValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NValue As System.Integer
Dim value As System.Integer

value = instance.SetExtraFrequenciesUnit(NValue)
```

### C#

```csharp
System.int SetExtraFrequenciesUnit(
   System.int NValue
)
```

### C++/CLI

```cpp
System.int SetExtraFrequenciesUnit(
   System.int NValue
)
```

### Parameters

- `NValue`: Units of extra frequencies as defined by [swsFrequencyUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyUnit_e.html)

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::SetExtraFrequenciesUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetExtraFrequenciesUnit.html).

## Remarks

This method:

- is valid only if [ICWDynamicStudyOptions::GetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html) is true.

- sets the units for extra frequency points which can also be set using the dialog opened by `Simulation Study (RMB)` **> Properties > Advanced > Extra points in addition to natural frequencies > Edit...**.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesUnit.html)
[ICWDynamicStudyOptions::SetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequencies.html)
[ICWDynamicStudyOptions::SetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::SetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
