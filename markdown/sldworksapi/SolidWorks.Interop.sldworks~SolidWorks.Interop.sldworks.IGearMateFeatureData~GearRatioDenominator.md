---
title: "GearRatioDenominator Property (IGearMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGearMateFeatureData"
member: "GearRatioDenominator"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~GearRatioDenominator.html"
---

# GearRatioDenominator Property (IGearMateFeatureData)

Gets or sets the denominator of the gear ratio of this gear mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property GearRatioDenominator As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGearMateFeatureData
Dim value As System.Double

instance.GearRatioDenominator = value

value = instance.GearRatioDenominator
```

### C#

```csharp
System.double GearRatioDenominator {get; set;}
```

### C++/CLI

```cpp
property System.double GearRatioDenominator {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gear ratio denominator

## VBA Syntax

See [GearMateFeatureData::GearRatioDenominator](ms-its:sldworksapivb6.chm::/sldworks~GearMateFeatureData~GearRatioDenominator.html).

## Examples

See the [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html) example.

## See Also

[IGearMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html)
[IGearMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.html)
[IGearMateFeatureData::GearRatioNumerator Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~GearRatioNumerator.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
