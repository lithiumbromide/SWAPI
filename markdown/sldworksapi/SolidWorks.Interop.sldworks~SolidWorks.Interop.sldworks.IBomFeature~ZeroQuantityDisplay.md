---
title: "ZeroQuantityDisplay Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "ZeroQuantityDisplay"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ZeroQuantityDisplay.html"
---

# ZeroQuantityDisplay Property (IBomFeature)

Gets or sets the character or value to display when a value is 0 in this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property ZeroQuantityDisplay As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Integer

instance.ZeroQuantityDisplay = value

value = instance.ZeroQuantityDisplay
```

### C#

```csharp
System.int ZeroQuantityDisplay {get; set;}
```

### C++/CLI

```cpp
property System.int ZeroQuantityDisplay {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Character or value to display when value is 0 as defined by [swZeroQuantityDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swZeroQuantityDisplay_e.html)

## VBA Syntax

See [BomFeature::ZeroQuantityDisplay](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~ZeroQuantityDisplay.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
