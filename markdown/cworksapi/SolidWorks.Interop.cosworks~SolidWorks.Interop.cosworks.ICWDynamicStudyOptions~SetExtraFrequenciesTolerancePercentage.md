---
title: "SetExtraFrequenciesTolerancePercentage Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetExtraFrequenciesTolerancePercentage"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesTolerancePercentage.html"
---

# SetExtraFrequenciesTolerancePercentage Method (ICWDynamicStudyOptions)

Sets the tolerance for merging extra frequency points with nearby natural frequency points.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExtraFrequenciesTolerancePercentage( _
   ByVal DValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DValue As System.Double
Dim value As System.Integer

value = instance.SetExtraFrequenciesTolerancePercentage(DValue)
```

### C#

```csharp
System.int SetExtraFrequenciesTolerancePercentage(
   System.double DValue
)
```

### C++/CLI

```cpp
System.int SetExtraFrequenciesTolerancePercentage(
   System.double DValue
)
```

### Parameters

- `DValue`: Extra frequency points merge tolerance

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::SetExtraFrequenciesTolerancePercentage](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetExtraFrequenciesTolerancePercentage.html).

## Remarks

This method:

- is valid only if [ICWDynamicStudyOptions::GetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html) is true.

- sets a merge tolerance percentage which can also be set using `Simulation Study (RMB)` **> Properties > Advanced > Tolerance to merge frequency points (%).** An extra frequency point is merged with its nearest natural frequency point if their frequency difference is within this tolerance.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::SetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequencies.html)
[ICWDynamicStudyOptions::SetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesUnit.html)
[ICWDynamicStudyOptions::SetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
