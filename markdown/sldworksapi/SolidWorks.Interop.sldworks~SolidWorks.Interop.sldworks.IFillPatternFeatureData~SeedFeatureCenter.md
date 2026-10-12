---
title: "SeedFeatureCenter Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "SeedFeatureCenter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenter.html"
---

# SeedFeatureCenter Property (IFillPatternFeatureData)

Gets or sets the vertex or sketch point where to place the center of the seed cut feature of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SeedFeatureCenter As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Object

instance.SeedFeatureCenter = value

value = instance.SeedFeatureCenter
```

### C#

```csharp
System.object SeedFeatureCenter {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SeedFeatureCenter {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) or [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) where to place the center of the seed cut feature

## VBA Syntax

See [FillPatternFeatureData::SeedFeatureCenter](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~SeedFeatureCenter.html).

## Remarks

This property is valid only if [IFillPatternFeatureData::FeaturesToPatternType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.html) = [swFeaturesToPatternType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html).swFeaturesToPatternCreateSeedCut.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)
[IFillPatternFeatureData::SeedFeatureCenterType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenterType.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
