---
title: "Dimension Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "Dimension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Dimension.html"
---

# Dimension Property (IFillPatternFeatureData)

Gets or sets the length of a side of a diamond-cut or square-cut seed instance of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Dimension As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Double

instance.Dimension = value

value = instance.Dimension
```

### C#

```csharp
System.double Dimension {get; set;}
```

### C++/CLI

```cpp
property System.double Dimension {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of side of diamond-cut or square-cut seed instance

## VBA Syntax

See [FillPatternFeatureData::Dimension](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~Dimension.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

This property is valid only if both are true:

- [IFillPatternFeatureData::FeaturesToPatternType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.html) = [swFeaturesToPatternType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html).swFeaturesToPatternCreateSeedCut
- [IFillPatternFeatureData::CreateSeedCutType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType.html) is set to one of the following:

  - [swCreateSeedCutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSeedCutType_e.html).swCreateSeedCutDiamond
  - swCreateSeedCutType_e.swCreateSeedCutSquare

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
