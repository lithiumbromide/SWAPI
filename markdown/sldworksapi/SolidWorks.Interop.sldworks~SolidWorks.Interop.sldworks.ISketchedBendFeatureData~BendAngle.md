---
title: "BendAngle Property (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "BendAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~BendAngle.html"
---

# BendAngle Property (ISketchedBendFeatureData)

Gets or sets the bend angle of this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim value As System.Double

instance.BendAngle = value

value = instance.BendAngle
```

### C#

```csharp
System.double BendAngle {get; set;}
```

### C++/CLI

```cpp
property System.double BendAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.261799 <= Bend angle in increments of 0.261799 radians (15 degrees) <= 1.5708

## VBA Syntax

See [SketchedBendFeatureData::BendAngle](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~BendAngle.html).

## Examples

See the [ISketchedBendFeatureData::OverrideValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~OverrideValue.html) examples.

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
