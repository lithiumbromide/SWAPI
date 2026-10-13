---
title: "PatternElement Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "PatternElement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternElement.html"
---

# PatternElement Property (IFillPatternFeatureData)

Gets or sets the pattern element selection of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternElement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
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

Pattern element selection as defined in [swPatternElementSelection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html)

## VBA Syntax

See [FillPatternFeatureData::PatternElement](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~PatternElement.html).

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
