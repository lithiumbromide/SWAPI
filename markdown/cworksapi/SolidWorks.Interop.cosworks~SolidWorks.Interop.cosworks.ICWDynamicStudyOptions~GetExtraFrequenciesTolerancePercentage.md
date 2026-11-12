---
title: "GetExtraFrequenciesTolerancePercentage Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetExtraFrequenciesTolerancePercentage"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTolerancePercentage.html"
---

# GetExtraFrequenciesTolerancePercentage Method (ICWDynamicStudyOptions)

Gets the tolerance for merging extra frequency points with nearby natural frequency points.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtraFrequenciesTolerancePercentage( _
   ByRef DValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DValue As System.Double
Dim value As System.Integer

value = instance.GetExtraFrequenciesTolerancePercentage(DValue)
```

### C#

```csharp
System.int GetExtraFrequenciesTolerancePercentage(
   out System.double DValue
)
```

### C++/CLI

```cpp
System.int GetExtraFrequenciesTolerancePercentage(
   [Out] System.double DValue
)
```

### Parameters

- `DValue`: Extra frequency points merge tolerance

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::GetExtraFrequenciesTolerancePercentage](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetExtraFrequenciesTolerancePercentage.html).

## Remarks

This method:

- is valid only if [ICWDynamicStudyOptions::GetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html) is true.

- gets the tolerance percentage that is shown in `Simulation Study (RMB)` **> Properties > Advanced > Tolerance to merge frequency points (%).** An extra frequency point is merged with its nearest natural frequency point if their frequency difference is within this tolerance.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::GetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequencies.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTotal Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTotal.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesUnit.html)
[ICWDynamicStudyOptions::SetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
