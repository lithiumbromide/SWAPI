---
title: "GeometryPattern Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "GeometryPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~GeometryPattern.html"
---

# GeometryPattern Property (IFillPatternFeatureData)

Gets or sets whether to create this fill pattern using an exact copy of the seed feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GeometryPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Boolean

instance.GeometryPattern = value

value = instance.GeometryPattern
```

### C#

```csharp
System.bool GeometryPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool GeometryPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create the pattern using an exact copy of the seed feature, false to solve individual instances of the seed feature

## VBA Syntax

See [FillPatternFeatureData::GeometryPattern](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~GeometryPattern.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

This property is valid only if [IFillPatternFeatureData::PatternElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternElement.html) is [swPatternElementSelection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html).swFeatureFaces.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
