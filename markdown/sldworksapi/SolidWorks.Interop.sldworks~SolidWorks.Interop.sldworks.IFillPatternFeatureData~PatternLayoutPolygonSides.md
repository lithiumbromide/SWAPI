---
title: "PatternLayoutPolygonSides Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "PatternLayoutPolygonSides"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutPolygonSides.html"
---

# PatternLayoutPolygonSides Property (IFillPatternFeatureData)

Gets or sets the number of sides in the polygonal layout of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternLayoutPolygonSides As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

instance.PatternLayoutPolygonSides = value

value = instance.PatternLayoutPolygonSides
```

### C#

```csharp
System.int PatternLayoutPolygonSides {get; set;}
```

### C++/CLI

```cpp
property System.int PatternLayoutPolygonSides {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of sides in the polygonal layout of this fill pattern

## VBA Syntax

See [FillPatternFeatureData::PatternLayoutPolygonSides](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~PatternLayoutPolygonSides.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

This property is valid only if [IFillPatternFeatureData::PatternLayoutType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.html) = [swPatternLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html).swPatternLayoutPolygon.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
