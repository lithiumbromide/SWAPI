---
title: "SeedCutFlipShapeDirection Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "SeedCutFlipShapeDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedCutFlipShapeDirection.html"
---

# SeedCutFlipShapeDirection Property (IFillPatternFeatureData)

Gets or sets whether to reverse the direction of the seed instance cut of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SeedCutFlipShapeDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Boolean

instance.SeedCutFlipShapeDirection = value

value = instance.SeedCutFlipShapeDirection
```

### C#

```csharp
System.bool SeedCutFlipShapeDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool SeedCutFlipShapeDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of the seed instance cut, false to not

## VBA Syntax

See [FillPatternFeatureData::SeedCutFlipShapeDirection](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~SeedCutFlipShapeDirection.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

This property is valid only if [IFillPatternFeatureData::FeaturesToPatternType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.html) = [swFeaturesToPatternType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html).swFeaturesToPatternCreateSeedCut.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)
[IFillPatternFeatureData::CreateSeedCutType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
