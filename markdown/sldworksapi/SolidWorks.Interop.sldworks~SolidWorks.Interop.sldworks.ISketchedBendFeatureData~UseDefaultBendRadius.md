---
title: "UseDefaultBendRadius Property (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "UseDefaultBendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseDefaultBendRadius.html"
---

# UseDefaultBendRadius Property (ISketchedBendFeatureData)

Gets or sets whether to use the default bend radius of this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim value As System.Boolean

instance.UseDefaultBendRadius = value

value = instance.UseDefaultBendRadius
```

### C#

```csharp
System.bool UseDefaultBendRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the default bend radius, false to specify another bend radius

## VBA Syntax

See [SketchedBendFeatureData::UseDefaultBendRadius](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~UseDefaultBendRadius.html).

## Examples

See [ISketchedBendFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchedBendFeatureData.html) examples.

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## Remarks

This property takes precedence over [ISketchedBendFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseGaugeTable.html). If this property is set to true, then ISketchedBendFeatureData::UseGaugeTable is set to false and cannot be changed.

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)
[ISketchedBendFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~BendRadius.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
