---
title: "D2Spacing Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D2Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2Spacing.html"
---

# D2Spacing Property (ICurveDrivenPatternFeatureData)

Gets or sets the spacing of pattern instances in Direction 2 for this bidirectional curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Double

instance.D2Spacing = value

value = instance.D2Spacing
```

### C#

```csharp
System.double D2Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double D2Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern spacing

## VBA Syntax

See [CurveDrivenPatternFeatureData::D2Spacing](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D2Spacing.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1Spacing.html)
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
