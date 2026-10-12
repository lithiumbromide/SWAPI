---
title: "Group1FlipPlane Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Group1FlipPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1FlipPlane.html"
---

# Group1FlipPlane Property (IChainPatternFeatureData)

Gets or sets whether to flip the [position plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.html) for **Chain Group 1** in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Group1FlipPlane As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Boolean

instance.Group1FlipPlane = value

value = instance.Group1FlipPlane
```

### C#

```csharp
System.bool Group1FlipPlane {get; set;}
```

### C++/CLI

```cpp
property System.bool Group1FlipPlane {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the position plane, false to not

## VBA Syntax

See [ChainPatternFeatureData::Group1FlipPlane](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Group1FlipPlane.html).

## Remarks

This property is available for all types of chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::Group1PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink1.html)
[IChainPatternFeatureData::Group1PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink2.html)
[IChainPatternFeatureData::Group1PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathPlane.html)
[IChainPatternFeatureData::Group1PatternComponent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PatternComponent.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
