---
title: "SeedFeatureCenterType Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "SeedFeatureCenterType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenterType.html"
---

# SeedFeatureCenterType Property (IFillPatternFeatureData)

Gets or sets the type of entity where to place the center of the seed cut feature for this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SeedFeatureCenterType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

value = instance.SeedFeatureCenterType
```

### C#

```csharp
System.int SeedFeatureCenterType {get;}
```

### C++/CLI

```cpp
property System.int SeedFeatureCenterType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [FillPatternFeatureData::SeedFeatureCenterType](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~SeedFeatureCenterType.html).

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)
[IFillPatternFeatureData::SeedFeatureCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenter.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
