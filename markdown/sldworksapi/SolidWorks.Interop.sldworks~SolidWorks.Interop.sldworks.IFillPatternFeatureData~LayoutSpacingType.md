---
title: "LayoutSpacingType Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "LayoutSpacingType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~LayoutSpacingType.html"
---

# LayoutSpacingType Property (IFillPatternFeatureData)

Gets or sets the type of spacing between the instances in the layout of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property LayoutSpacingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

instance.LayoutSpacingType = value

value = instance.LayoutSpacingType
```

### C#

```csharp
System.int LayoutSpacingType {get; set;}
```

### C++/CLI

```cpp
property System.int LayoutSpacingType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern layout spacing type as defined in [swPatternLayoutSpacingType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutSpacingType_e.html)

## VBA Syntax

See [FillPatternFeatureData::LayoutSpacingType](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~LayoutSpacingType.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

| If this property is set to... | Then also set... |
| --- | --- |
| swPatternLayoutSpacingType_e.swPatternLayoutInstances | IFillPatternFeatureData::NoOfInstances ; IFillPatternFeatureData::InstanceSpacing is not valid |
| swPatternLayoutSpacingType_e.swPatternLayoutTargetSpacing | IFillPatternFeatureData::InstanceSpacing; IFillPatternFeatureData::NoOfInstances is not valid |

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)
[IFillPatternFeatureData::PatternLayoutType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
