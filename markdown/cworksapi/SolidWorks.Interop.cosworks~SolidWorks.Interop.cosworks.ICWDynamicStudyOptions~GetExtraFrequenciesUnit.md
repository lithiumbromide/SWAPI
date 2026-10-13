---
title: "GetExtraFrequenciesUnit Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetExtraFrequenciesUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesUnit.html"
---

# GetExtraFrequenciesUnit Method (ICWDynamicStudyOptions)

Gets the units of extra frequencies.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtraFrequenciesUnit( _
   ByRef NValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NValue As System.Integer
Dim value As System.Integer

value = instance.GetExtraFrequenciesUnit(NValue)
```

### C#

```csharp
System.int GetExtraFrequenciesUnit(
   out System.int NValue
)
```

### C++/CLI

```cpp
System.int GetExtraFrequenciesUnit(
   [Out] System.int NValue
)
```

### Parameters

- `NValue`: Units of extra frequencies as defined by [swsFrequencyUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyUnit_e.html)

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::GetExtraFrequenciesUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetExtraFrequenciesUnit.html).

## Remarks

This method:

- is valid only if [ICWDynamicStudyOptions::GetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html) is true.

- gets the units for extra frequency points that a shown in the dialog opened by `Simulation Study (RMB)` **> Properties > Advanced > Extra points in addition to natural frequencies > Edit...**.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesUnit.html)
[ICWDynamicStudyOptions::GetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequencies.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTotal Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTotal.html)
[ICWDynamicStudyOptions::SetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
