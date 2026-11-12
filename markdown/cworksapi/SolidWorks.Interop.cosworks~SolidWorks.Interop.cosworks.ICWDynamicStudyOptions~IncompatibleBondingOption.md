---
title: "IncompatibleBondingOption Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "IncompatibleBondingOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~IncompatibleBondingOption.html"
---

# IncompatibleBondingOption Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetIncompatibleBondingOption2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetIncompatibleBondingOption2.html) and [ICWDynamicStudyOptions::SetIncompatibleBondingOption2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetIncompatibleBondingOption2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property IncompatibleBondingOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.IncompatibleBondingOption = value

value = instance.IncompatibleBondingOption
```

### C#

```csharp
System.int IncompatibleBondingOption {get; set;}
```

### C++/CLI

```cpp
property System.int IncompatibleBondingOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Option as defined in [swsIncompatibleBondingOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsIncompatibleBondingOption_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::IncompatibleBondingOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~IncompatibleBondingOption.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
