---
title: "SeedPosition Property (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "SeedPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~SeedPosition.html"
---

# SeedPosition Property (IDerivedPatternFeatureData)

Gets or sets which pattern instance to use as the seed feature for this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SeedPosition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
Dim value As System.Integer

instance.SeedPosition = value

value = instance.SeedPosition
```

### C#

```csharp
System.int SeedPosition {get; set;}
```

### C++/CLI

```cpp
property System.int SeedPosition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern instance to use as the seed feature (see **Remarks**)

## VBA Syntax

See [DerivedPatternFeatureData::SeedPosition](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData~SeedPosition.html).

## Examples

[Create Derived Pattern Feature (C#)](Create_Derived_Pattern_Feature_Example_CSharp.htm)
[Create Derived Pattern Feature (VB.NET)](Create_Derived_Pattern_Feature_Example_VBNET.htm)
[Create Derived Pattern Feature (VBA)](Create_Derived_Pattern_Feature_Example_VB.htm)

## Remarks

The seed position is the index of a pattern instance, feature, or component that is part of an existing pattern and is used to drive the derived pattern feature.

The total number of seed positions = total number of pattern instances in the pattern used to create the derived pattern feature.

If the pattern used to create the derived pattern has pattern instances in Direction 1 and Direction 2, then the total number of seed positions = ((Number pattern instances in Direction 1) * (Number pattern instances in Direction 2) - 1).

Setting the seed position outside of the range of pattern instances is silently rejected, and the seed position remains unchanged.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
