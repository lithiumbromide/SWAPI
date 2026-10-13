---
title: "LoopSpacing Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "LoopSpacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~LoopSpacing.html"
---

# LoopSpacing Property (IFillPatternFeatureData)

Gets or sets the distance between loops of pattern instances in this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoopSpacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Double

instance.LoopSpacing = value

value = instance.LoopSpacing
```

### C#

```csharp
System.double LoopSpacing {get; set;}
```

### C++/CLI

```cpp
property System.double LoopSpacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between loops of pattern instances

## VBA Syntax

See [FillPatternFeatureData::LoopSpacing](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~LoopSpacing.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

All fill patterns except those with perforated layouts are created by positioning a pattern seed instance within the fill boundary and copying the pattern in concentric loops about the seed instance. This property sets the spacing between the centers of instances in adjacent pattern loops.

This property is valid only if [IFillPatternFeatureData::PatternLayoutType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.html) is set to one of the following:

- [swPatternLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html).swPatternLayoutCircular
- swPatternLayoutType_e.swPatternLayoutPolygon
- swPatternLayoutType_e.swPatternLayoutSquare

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
