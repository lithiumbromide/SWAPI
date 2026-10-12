---
title: "PatternElement Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "PatternElement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternElement.html"
---

# PatternElement Property (ISketchPatternFeatureData)

Gets or sets the type of entities to base this sketch pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternElement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
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

Type of entities to base this sketch pattern feature as defined in [swPatternElementSelection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html)

## VBA Syntax

See [SketchPatternFeatureData::PatternElement](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~PatternElement.html).

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::BodyPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
