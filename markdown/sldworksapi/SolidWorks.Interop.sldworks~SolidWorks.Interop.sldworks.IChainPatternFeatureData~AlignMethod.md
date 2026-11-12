---
title: "AlignMethod Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "AlignMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~AlignMethod.html"
---

# AlignMethod Property (IChainPatternFeatureData)

Gets or sets how to align this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlignMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Integer

instance.AlignMethod = value

value = instance.AlignMethod
```

### C#

```csharp
System.int AlignMethod {get; set;}
```

### C++/CLI

```cpp
property System.int AlignMethod {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Align method as defined in [swChainPatternAlignment_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChainPatternAlignment_e.html) (see **Remarks**)

## VBA Syntax

See [ChainPatternFeatureData::AlignMethod](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~AlignMethod.html).

## Remarks

This property is only available for distance chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
