---
title: "SetIncludeExtraFrequencies Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetIncludeExtraFrequencies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html"
---

# SetIncludeExtraFrequencies Method (ICWDynamicStudyOptions)

Sets whether to include extra frequency points in the analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIncludeExtraFrequencies( _
   ByVal BChecked As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Boolean
Dim value As System.Integer

value = instance.SetIncludeExtraFrequencies(BChecked)
```

### C#

```csharp
System.int SetIncludeExtraFrequencies(
   System.bool BChecked
)
```

### C++/CLI

```cpp
System.int SetIncludeExtraFrequencies(
   System.bool BChecked
)
```

### Parameters

- `BChecked`: True to include extra frequency points, false to not

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::SetIncludeExtraFrequencies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetIncludeExtraFrequencies.html).

## Remarks

This method corresponds to the setting of `Simulation Study (RMB)` **> Properties > Advanced > Extra points in addition to natural frequencies.**

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html)
[ICWDynamicStudyOptions::SetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequencies.html)
[ICWDynamicStudyOptions::SetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::SetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesUnit.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
