---
title: "CreateSeedCutPolygonSides Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "CreateSeedCutPolygonSides"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutPolygonSides.html"
---

# CreateSeedCutPolygonSides Property (IFillPatternFeatureData)

Gets or sets the number of sides in a polygon-cut seed instance of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CreateSeedCutPolygonSides As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

instance.CreateSeedCutPolygonSides = value

value = instance.CreateSeedCutPolygonSides
```

### C#

```csharp
System.int CreateSeedCutPolygonSides {get; set;}
```

### C++/CLI

```cpp
property System.int CreateSeedCutPolygonSides {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of sides in a polygon-cut seed instance

## VBA Syntax

See [FillPatternFeatureData::CreateSeedCutPolygonSides](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~CreateSeedCutPolygonSides.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

This property is valid only if both are true:

- [IFillPatternFeatureData::FeaturesToPatternType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.html) = [swFeaturesToPatternType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html).swFeaturesToPatternCreateSeedCut
- [IFillPatternFeatureData::CreateSeedCutType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType.html) = [swCreateSeedCutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSeedCutType_e.html).swCreateSeedCutPolygon

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
