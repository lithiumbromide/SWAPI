---
title: "SetExtraFrequencies Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetExtraFrequencies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequencies.html"
---

# SetExtraFrequencies Method (ICWDynamicStudyOptions)

Sets frequencies other than natural frequencies for this random vibration or harmonic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExtraFrequencies( _
   ByVal VarValues As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim VarValues As System.Object
Dim value As System.Integer

value = instance.SetExtraFrequencies(VarValues)
```

### C#

```csharp
System.int SetExtraFrequencies(
   System.object VarValues
)
```

### C++/CLI

```cpp
System.int SetExtraFrequencies(
   System.Object^ VarValues
)
```

### Parameters

- `VarValues`: Array of up to 20 extra frequencies

### Return Value

Error code as defined by [swsDynamicExtraFrequenciesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::SetExtraFrequencies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetExtraFrequencies.html).

## Remarks

This method:

- is valid only if [ICWDynamicStudyOptions::GetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html) is true.

- sets extra frequency points which can also be set using the dialog opened by `Simulation Study (RMB)` **> Properties > Advanced > Extra points in addition to natural frequencies > Edit...**.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequencies.html)
[ICWDynamicStudyOptions::SetExtraFrequenciesTolerancePercentage Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesTolerancePercentage.html)
[ICWDynamicStudyOptions::SetExtraFrequenciesUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesUnit.html)
[ICWDynamicStudyOptions::SetIncludeExtraFrequencies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)

## Availability

SOLIDWORKS Simulation API 2024 SP1
