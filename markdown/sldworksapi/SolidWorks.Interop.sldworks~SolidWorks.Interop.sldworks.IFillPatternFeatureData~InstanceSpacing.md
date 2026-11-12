---
title: "InstanceSpacing Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "InstanceSpacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~InstanceSpacing.html"
---

# InstanceSpacing Property (IFillPatternFeatureData)

Gets or sets the distance between the pattern instance centers of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property InstanceSpacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Double

instance.InstanceSpacing = value

value = instance.InstanceSpacing
```

### C#

```csharp
System.double InstanceSpacing {get; set;}
```

### C++/CLI

```cpp
property System.double InstanceSpacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between pattern instance centers

## VBA Syntax

See [FillPatternFeatureData::InstanceSpacing](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~InstanceSpacing.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

| This property is.... | If... |
| --- | --- |
| Always valid | IFillPatternFeatureData::PatternLayoutType = swPatternLayoutType_e .swPatternLayoutPerforation |
| Only valid | Both are true: IFillPatternFeatureData::LayoutSpacingType = swPatternLayoutSpacingType_e .swPatternLayoutTargetSpacing And: IFillPatternFeatureData::PatternLayoutType is set to one of the following: swPatternLayoutType_e.swPatternLayoutCircle swPatternLayoutType_e.swPatternLayoutSquare swPatternLayoutType_e.swPatternLayoutPolygon |

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
