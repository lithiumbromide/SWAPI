---
title: "CreateSeedCutType Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "CreateSeedCutType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutType.html"
---

# CreateSeedCutType Property (IFillPatternFeatureData)

Gets or sets the type of cut for this fill pattern's seed instance.

## Syntax

### Visual Basic (Declaration)

```vb
Property CreateSeedCutType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

instance.CreateSeedCutType = value

value = instance.CreateSeedCutType
```

### C#

```csharp
System.int CreateSeedCutType {get; set;}
```

### C++/CLI

```cpp
property System.int CreateSeedCutType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of seed instance cut as defined in [swCreateSeedCutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSeedCutType_e.html)

## VBA Syntax

See [FillPatternFeatureData::CreateSeedCutType](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~CreateSeedCutType.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)
[IFillPatternFeatureData::Diameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Diameter.html)
[IFillPatternFeatureData::Dimension Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Dimension.html)
[IFillPatternFeatureData::Diagonal Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Diagonal.html)
[IFillPatternFeatureData::Rotation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~Rotation.html)
[IFillPatternFeatureData::CreateSeedCutPolygonSides Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~CreateSeedCutPolygonSides.html)
[IFillPatternFeatureData::InnerRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~InnerRadius.html)
[IFillPatternFeatureData::OuterRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~OuterRadius.html)
[IFillPatternFeatureData::SeedCutFlipShapeDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedCutFlipShapeDirection.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
