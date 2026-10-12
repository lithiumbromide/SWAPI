---
title: "PatternBodyArray Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "PatternBodyArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternBodyArray.html"
---

# PatternBodyArray Property (IFillPatternFeatureData)

Gets or sets the array of bodies to pattern in this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternBodyArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Object

instance.PatternBodyArray = value

value = instance.PatternBodyArray
```

### C#

```csharp
System.object PatternBodyArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternBodyArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)s to pattern

## VBA Syntax

See [FillPatternFeatureData::PatternBodyArray](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~PatternBodyArray.html).

## Remarks

This property is valid only if [IFillPatternFeatureData::PatternElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternElement.html) is [swPatternElementSelection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html).swBodiesToPattern.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
