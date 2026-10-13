---
title: "PatternElement Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "PatternElement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternElement.html"
---

# PatternElement Property (ILinearPatternFeatureData)

Gets or sets the type of entities on which to base this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternElement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

Type of entities on which to base this linear pattern as defined in [swPatternElementSelection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html)

## VBA Syntax

See [LinearPatternFeatureData::PatternElement](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~PatternElement.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::BodyPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
