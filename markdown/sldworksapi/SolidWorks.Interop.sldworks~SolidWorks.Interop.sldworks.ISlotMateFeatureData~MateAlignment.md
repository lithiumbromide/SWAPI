---
title: "MateAlignment Property (ISlotMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISlotMateFeatureData"
member: "MateAlignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~MateAlignment.html"
---

# MateAlignment Property (ISlotMateFeatureData)

Gets or sets the mate alignment of this slot mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MateAlignment As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISlotMateFeatureData
Dim value As System.Integer

instance.MateAlignment = value

value = instance.MateAlignment
```

### C#

```csharp
System.int MateAlignment {get; set;}
```

### C++/CLI

```cpp
property System.int MateAlignment {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mate alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateAlign_e.html)

## VBA Syntax

See [SlotMateFeatureData::MateAlignment](ms-its:sldworksapivb6.chm::/sldworks~SlotMateFeatureData~MateAlignment.html).

## Examples

See the [ISlotMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html) example.

## See Also

[ISlotMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html)
[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
