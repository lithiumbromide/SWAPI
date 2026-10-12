---
title: "SeedAlignmentReferencePoint Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "SeedAlignmentReferencePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SeedAlignmentReferencePoint.html"
---

# SeedAlignmentReferencePoint Property (ILocalLinearPatternFeatureData)

Gets or sets the type of reference point with which to align each pattern instance to the seed feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SeedAlignmentReferencePoint As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Integer

instance.SeedAlignmentReferencePoint = value

value = instance.SeedAlignmentReferencePoint
```

### C#

```csharp
System.int SeedAlignmentReferencePoint {get; set;}
```

### C++/CLI

```cpp
property System.int SeedAlignmentReferencePoint {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Seed alignment reference point as defined in [swSeedAlignmentReferencePoint_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSeedAlignmentReferencePoint_e.html)

## VBA Syntax

See [LocalLinearPatternFeatureData::SeedAlignmentReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~SeedAlignmentReferencePoint.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::AlignToSeed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~AlignToSeed.html) is true.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
