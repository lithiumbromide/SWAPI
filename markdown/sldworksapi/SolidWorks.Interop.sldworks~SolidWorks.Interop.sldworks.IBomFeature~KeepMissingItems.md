---
title: "KeepMissingItems Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "KeepMissingItems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepMissingItems.html"
---

# KeepMissingItems Property (IBomFeature)

Gets and sets the Keep Missing Items option for this BOM feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepMissingItems As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Boolean

instance.KeepMissingItems = value

value = instance.KeepMissingItems
```

### C#

```csharp
System.bool KeepMissingItems {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepMissingItems {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to keep suppressed components, false to not

## VBA Syntax

See [BomFeature::KeepMissingItems](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~KeepMissingItems.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## Remarks

Missing items are suppressed components.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::StrikeoutMissingItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~StrikeoutMissingItems.html)
[IBomFeature::KeepReplacedCompOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepReplacedCompOption.html)

## Availability

SOLIDWORKS 2004 FCS, Revision number 12
