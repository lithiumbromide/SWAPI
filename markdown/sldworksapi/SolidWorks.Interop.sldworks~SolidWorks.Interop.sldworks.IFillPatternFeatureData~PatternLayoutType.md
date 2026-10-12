---
title: "PatternLayoutType Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "PatternLayoutType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.html"
---

# PatternLayoutType Property (IFillPatternFeatureData)

Gets or sets the layout of the pattern instances within the fill boundary of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternLayoutType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

instance.PatternLayoutType = value

value = instance.PatternLayoutType
```

### C#

```csharp
System.int PatternLayoutType {get; set;}
```

### C++/CLI

```cpp
property System.int PatternLayoutType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fill pattern layout type as defined in [swPatternLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html)

## VBA Syntax

See [FillPatternFeatureData::PatternLayoutType](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~PatternLayoutType.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

After specifying this property, specify the following:

- [IFillPatternFeatureData::Margins](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~Margins.html)
- [IFillPatternFeatureData::PatternDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternDirection.html)
- [IFillPatternFeatureData::GeometryPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~GeometryPattern.html)
- [IFillPatternFeatureData::PropagateVisualProperty](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PropagateVisualProperty.html)
- [IFillPatternFeatureData::FeaturesToPatternType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~FeaturesToPatternType.html)

Specify other properties as required by the settings above.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
