---
title: "GetExtraFrequenciesTotal Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetExtraFrequenciesTotal"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTotal.html"
---

# GetExtraFrequenciesTotal Method (ICWDynamicStudyOptions)

Gets the total number of extra frequency points.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtraFrequenciesTotal( _
   ByRef NValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NValue As System.Integer
Dim value As System.Integer

value = instance.GetExtraFrequenciesTotal(NValue)
```

### C#

```csharp
System.int GetExtraFrequenciesTotal(
   out System.int NValue
)
```

### C++/CLI

```cpp
System.int GetExtraFrequenciesTotal(
   [Out] System.int NValue
)
```

### Parameters

- `NValue`: Total number of extra frequency points

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::GetExtraFrequenciesTotal](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetExtraFrequenciesTotal.html).

## Remarks

This method

- is valid only if [ICWDynamicStudyOptions::GetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html) is true.
- gets the total number of extra frequencies as shown in the dialog opened by `Simulation Study (RMB)` **> Properties > Advanced > Extra points in addition to natural frequencies > Edit...**.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequencies.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesUnit.html)
[ICWDynamicStudyOptions::SetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
