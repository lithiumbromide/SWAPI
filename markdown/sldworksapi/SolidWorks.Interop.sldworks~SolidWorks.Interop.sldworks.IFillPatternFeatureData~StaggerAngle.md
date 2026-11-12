---
title: "StaggerAngle Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "StaggerAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~StaggerAngle.html"
---

# StaggerAngle Property (IFillPatternFeatureData)

Gets or sets the angle by which to stagger the rows of pattern instances in the perforation layout of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property StaggerAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Double

instance.StaggerAngle = value

value = instance.StaggerAngle
```

### C#

```csharp
System.double StaggerAngle {get; set;}
```

### C++/CLI

```cpp
property System.double StaggerAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Stagger angle for perforation layout

## VBA Syntax

See [FillPatternFeatureData::StaggerAngle](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~StaggerAngle.html).

## Examples

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html) example.

## Remarks

This property is valid only if [IFillPatternFeatureData::PatternLayoutType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.html) = [swPatternLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html).swPatternLayoutPerforation

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
