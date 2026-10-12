---
title: "SetIncompatibleBondingOption2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetIncompatibleBondingOption2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncompatibleBondingOption2.html"
---

# SetIncompatibleBondingOption2 Method (ICWDynamicStudyOptions)

Sets the bonding contact method used to analyze models that contain contacting surfaces with incompatible meshes.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIncompatibleBondingOption2( _
   ByVal NBondingOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NBondingOption As System.Integer
Dim value As System.Integer

value = instance.SetIncompatibleBondingOption2(NBondingOption)
```

### C#

```csharp
System.int SetIncompatibleBondingOption2(
   System.int NBondingOption
)
```

### C++/CLI

```cpp
System.int SetIncompatibleBondingOption2(
   System.int NBondingOption
)
```

### Parameters

- `NBondingOption`: Option as defined in [swsIncompatibleBondingOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsIncompatibleBondingOption_e.html)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetIncompatibleBondingOption2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetIncompatibleBondingOption2.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetIncompatibleBondingOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncompatibleBondingOption2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
