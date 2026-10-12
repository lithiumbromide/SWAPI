---
title: "NoOfInstances Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "NoOfInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~NoOfInstances.html"
---

# NoOfInstances Property (IFillPatternFeatureData)

Gets or sets the number of instances per loop or side of the layout of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property NoOfInstances As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

instance.NoOfInstances = value

value = instance.NoOfInstances
```

### C#

```csharp
System.int NoOfInstances {get; set;}
```

### C++/CLI

```cpp
property System.int NoOfInstances {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of instances per loop or side of the pattern layout

## VBA Syntax

See [FillPatternFeatureData::NoOfInstances](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~NoOfInstances.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

This property is valid only if both are true:

- [IFillPatternFeatureData::LayoutSpacingType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~LayoutSpacingType.html) = [swPatternLayoutSpacingType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutSpacingType_e.html).swPatternLayoutInstances

And:

- [IFillPatternFeatureData::PatternLayoutType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.html) is set to one of the following:

  - [swPatternLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html).swPatternLayoutCircular
  - swPatternLayoutType_e.swPatternLayoutPolygon
  - swPatternLayoutType_e.swPatternLayoutSquare

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
