---
title: "GetIncompatibleBondingOption2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetIncompatibleBondingOption2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncompatibleBondingOption2.html"
---

# GetIncompatibleBondingOption2 Method (ICWDynamicStudyOptions)

Gets the bonding contact method used to analyze models that contain contacting surfaces with incompatible meshes.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIncompatibleBondingOption2( _
   ByRef NBondingOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NBondingOption As System.Integer
Dim value As System.Integer

value = instance.GetIncompatibleBondingOption2(NBondingOption)
```

### C#

```csharp
System.int GetIncompatibleBondingOption2(
   out System.int NBondingOption
)
```

### C++/CLI

```cpp
System.int GetIncompatibleBondingOption2(
   [Out] System.int NBondingOption
)
```

### Parameters

- `NBondingOption`: Option as defined in [swsIncompatibleBondingOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsIncompatibleBondingOption_e.html)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetIncompatibleBondingOption2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetIncompatibleBondingOption2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetIncompatibleBondingOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncompatibleBondingOption2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
