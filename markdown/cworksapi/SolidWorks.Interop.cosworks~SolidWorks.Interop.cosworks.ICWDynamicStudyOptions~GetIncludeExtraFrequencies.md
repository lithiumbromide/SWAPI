---
title: "GetIncludeExtraFrequencies Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetIncludeExtraFrequencies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html"
---

# GetIncludeExtraFrequencies Method (ICWDynamicStudyOptions)

Gets whether to include extra frequency points in the analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIncludeExtraFrequencies( _
   ByRef BChecked As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Boolean
Dim value As System.Integer

value = instance.GetIncludeExtraFrequencies(BChecked)
```

### C#

```csharp
System.int GetIncludeExtraFrequencies(
   out System.bool BChecked
)
```

### C++/CLI

```cpp
System.int GetIncludeExtraFrequencies(
   [Out] System.bool BChecked
)
```

### Parameters

- `BChecked`: True to include extra frequency points, false to not

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::GetIncludeExtraFrequencies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetIncludeExtraFrequencies.html).

## Remarks

This method gets the setting of `Simulation Study (RMB)` **> Properties > Advanced > Extra points in addition to natural frequencies.**

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)
[ICWDynamicStudyOptions::GetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequencies.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTotal Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTotal.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesUnit.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
