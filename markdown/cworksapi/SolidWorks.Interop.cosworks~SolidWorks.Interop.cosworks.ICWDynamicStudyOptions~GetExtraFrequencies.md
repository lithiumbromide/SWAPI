---
title: "GetExtraFrequencies Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetExtraFrequencies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequencies.html"
---

# GetExtraFrequencies Method (ICWDynamicStudyOptions)

Gets frequencies other than natural frequencies for this random vibration or harmonic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtraFrequencies( _
   ByRef VarValues As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim VarValues As System.Object
Dim value As System.Integer

value = instance.GetExtraFrequencies(VarValues)
```

### C#

```csharp
System.int GetExtraFrequencies(
   out System.object VarValues
)
```

### C++/CLI

```cpp
System.int GetExtraFrequencies(
   [Out] System.Object^ VarValues
)
```

### Parameters

- `VarValues`: Array of up to 20 extra frequencies

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::GetExtraFrequencies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetExtraFrequencies.html).

## Remarks

This method:

- is valid only if [ICWDynamicStudyOptions::GetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html) is true.

- gets the extra points that are set in the dialog opened by `Simulation Study (RMB)` **> Properties > Advanced > Extra points in addition to natural frequencies > Edit...**.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequencies.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTotal Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTotal.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesUnit.html)
[ICWDynamicStudyOptions::SetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
