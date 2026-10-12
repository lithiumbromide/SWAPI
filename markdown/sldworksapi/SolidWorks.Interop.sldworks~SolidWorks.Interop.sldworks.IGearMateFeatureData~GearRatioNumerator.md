---
title: "GearRatioNumerator Property (IGearMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGearMateFeatureData"
member: "GearRatioNumerator"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~GearRatioNumerator.html"
---

# GearRatioNumerator Property (IGearMateFeatureData)

Gets or sets the numerator of the gear ratio of this gear mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property GearRatioNumerator As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGearMateFeatureData
Dim value As System.Double

instance.GearRatioNumerator = value

value = instance.GearRatioNumerator
```

### C#

```csharp
System.double GearRatioNumerator {get; set;}
```

### C++/CLI

```cpp
property System.double GearRatioNumerator {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gear ratio numerator

## VBA Syntax

See [GearMateFeatureData::GearRatioNumerator](ms-its:sldworksapivb6.chm::/sldworks~GearMateFeatureData~GearRatioNumerator.html).

## Examples

See the [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html) example.

## See Also

[IGearMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html)
[IGearMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.html)
[IGearMateFeatureData::GearRatioDenominator Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~GearRatioDenominator.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
