---
title: "Rotation Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "Rotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Rotation.html"
---

# Rotation Property (IFillPatternFeatureData)

Gets or sets the counterclockwise rotation of the seed instance of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Rotation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Double

instance.Rotation = value

value = instance.Rotation
```

### C#

```csharp
System.double Rotation {get; set;}
```

### C++/CLI

```cpp
property System.double Rotation {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Counterclockwise rotation of the seed instance

## VBA Syntax

See [FillPatternFeatureData::Rotation](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~Rotation.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

This property is valid only if both are true:

- [IFillPatternFeatureData::FeaturesToPatternType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.html) = [swFeaturesToPatternType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html).swFeaturesToPatternCreateSeedCut

And:

- [IFillPatternFeatureData::CreateSeedCutType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType.html) is set to one of the following:

  - [swCreateSeedCutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSeedCutType_e.html).swCreateSeedCutDiamond
  - swCreateSeedCutType_e.swCreateSeedCutPolygon
  - swCreateSeedCutType_e.swCreateSeedCutSquare

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
