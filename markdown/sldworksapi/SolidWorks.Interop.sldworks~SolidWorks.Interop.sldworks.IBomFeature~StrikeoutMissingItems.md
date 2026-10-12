---
title: "StrikeoutMissingItems Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "StrikeoutMissingItems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~StrikeoutMissingItems.html"
---

# StrikeoutMissingItems Property (IBomFeature)

Inserts a horizontal line through missing items in this BOM table (also called strike outs).

## Syntax

### Visual Basic (Declaration)

```vb
Property StrikeoutMissingItems As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Boolean

instance.StrikeoutMissingItems = value

value = instance.StrikeoutMissingItems
```

### C#

```csharp
System.bool StrikeoutMissingItems {get; set;}
```

### C++/CLI

```cpp
property System.bool StrikeoutMissingItems {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to strike out suppressed components, false to not

## VBA Syntax

See [BomFeature::StrikeoutMissingItems](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~StrikeoutMissingItems.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## Remarks

Missing items are suppressed components.

This property is valid only if [IBomFeature::KeepMissingItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~KeepMissingItems.html) is set to true.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::KeepReplacedCompOption Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepReplacedCompOption.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
