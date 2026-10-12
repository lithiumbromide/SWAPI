---
title: "PatternElement Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "PatternElement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternElement.html"
---

# PatternElement Property (ICircularPatternFeatureData)

Gets or sets the type of entities on which to base this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternElement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

Type of entities on which to base this circular pattern feature defined in [swPatternElementSelection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html)

## VBA Syntax

See [CircularPatternFeatureData::PatternElement](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~PatternElement.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::BodyPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
