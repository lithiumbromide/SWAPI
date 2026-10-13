---
title: "KeepReplacedCompOption Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "KeepReplacedCompOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepReplacedCompOption.html"
---

# KeepReplacedCompOption Property (IBomFeature)

Gets or sets how to replace components when keeping missing items.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepReplacedCompOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Integer

instance.KeepReplacedCompOption = value

value = instance.KeepReplacedCompOption
```

### C#

```csharp
System.int KeepReplacedCompOption {get; set;}
```

### C++/CLI

```cpp
property System.int KeepReplacedCompOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Option for replacing components as defined in [swKeepReplacedCompOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swKeepReplacedCompOption_e.html)

## VBA Syntax

See [BomFeature::KeepReplacedCompOption](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~KeepReplacedCompOption.html).

## Examples

See the [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html) examples.

## Remarks

This property is valid only if [IBomFeature::KeepMissingItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~KeepMissingItems.html) is set to true.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::StrikeoutMissingItems Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~StrikeoutMissingItems.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
