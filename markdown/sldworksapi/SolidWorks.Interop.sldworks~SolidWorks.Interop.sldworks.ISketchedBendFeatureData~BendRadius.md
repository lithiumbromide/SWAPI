---
title: "BendRadius Property (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "BendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~BendRadius.html"
---

# BendRadius Property (ISketchedBendFeatureData)

Gets or sets the bend radius of this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim value As System.Double

instance.BendRadius = value

value = instance.BendRadius
```

### C#

```csharp
System.double BendRadius {get; set;}
```

### C++/CLI

```cpp
property System.double BendRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend radius in meters

## VBA Syntax

See [SketchedBendFeatureData::BendRadius](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~BendRadius.html).

## Examples

See the [ISketchedBendFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchedBendFeatureData.html) and [ISketchedBendFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseGaugeTable.html) examples.

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## Remarks

This property is valid only if [ISketchedBendFeatureData::UseDefaultBendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseDefaultBendRadius.html) is false.

To use something other than the default bend radius, set:

- ISketchedBendFeatureData::UseDefaultBendRadius to false

- and -

- [ISketchedBendFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseGaugeTable.html) to false.

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
