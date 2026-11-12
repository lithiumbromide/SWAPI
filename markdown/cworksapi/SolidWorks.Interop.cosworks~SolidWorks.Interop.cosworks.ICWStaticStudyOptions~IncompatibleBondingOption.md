---
title: "IncompatibleBondingOption Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "IncompatibleBondingOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncompatibleBondingOption.html"
---

# IncompatibleBondingOption Property (ICWStaticStudyOptions)

Gets or sets the incompatible bonding option.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncompatibleBondingOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

Incompatible bonding option as defined in [swsIncompatibleBondingOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsIncompatibleBondingOption_e.html)

## VBA Syntax

See [CWStaticStudyOptions::IncompatibleBondingOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~IncompatibleBondingOption.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
