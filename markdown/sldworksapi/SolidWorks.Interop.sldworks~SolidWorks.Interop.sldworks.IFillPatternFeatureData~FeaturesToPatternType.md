---
title: "FeaturesToPatternType Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "FeaturesToPatternType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.html"
---

# FeaturesToPatternType Property (IFillPatternFeatureData)

Gets or sets the type of object to pattern in this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeaturesToPatternType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

instance.FeaturesToPatternType = value

value = instance.FeaturesToPatternType
```

### C#

```csharp
System.int FeaturesToPatternType {get; set;}
```

### C++/CLI

```cpp
property System.int FeaturesToPatternType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of object to pattern as defined in [swFeaturesToPatternType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html)

## VBA Syntax

See [FillPatternFeatureData::FeaturesToPatternType](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~FeaturesToPatternType.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

| If this property is set to... | Then call... |
| --- | --- |
| swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut | IFillPatternFeatureData::CreateSeedCutType to get or set the type of seed cut to pattern |
| swFeaturesToPatternType_e.swFeaturesToPatternSelectedFeatures | IFillPatternFeatureData::PatternFeatureArray to get or set the array of features to pattern IFillPatternFeatureData::PatternFaceArray to get or set the array of faces to pattern IFillPatternFeatureData::PatternBodyArray to get or set the array of bodies to pattern |

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
