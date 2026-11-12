---
title: "PatternElement Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "PatternElement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternElement.html"
---

# PatternElement Property (ICurveDrivenPatternFeatureData)

Gets or sets the type of entities to base this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternElement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer

instance.PatternElement = value

value = instance.PatternElement
```

### C#

```csharp
System.int PatternElement {get; set;}
```

### C++/CLI

```cpp
property System.int PatternElement {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of entities to base this curve-driven pattern feature as defined in [swPatternElementSelection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html)

## VBA Syntax

See [CurveDrivenPatternFeatureData::PatternElement](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~PatternElement.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::BodyPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
