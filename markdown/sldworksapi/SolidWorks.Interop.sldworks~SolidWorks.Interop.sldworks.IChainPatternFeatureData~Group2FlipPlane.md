---
title: "Group2FlipPlane Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Group2FlipPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2FlipPlane.html"
---

# Group2FlipPlane Property (IChainPatternFeatureData)

Gets or sets whether to flip the [position plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.html) for **Chain Group 2** in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Group2FlipPlane As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Boolean

instance.Group2FlipPlane = value

value = instance.Group2FlipPlane
```

### C#

```csharp
System.bool Group2FlipPlane {get; set;}
```

### C++/CLI

```cpp
property System.bool Group2FlipPlane {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the position plane, false to not

## VBA Syntax

See [ChainPatternFeatureData::Group2FlipPlane](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Group2FlipPlane.html).

## Remarks

This property is only available for connected linkage chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::Group2PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink1.html)
[IChainPatternFeatureData::Group2PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink2.html)
[IChainPatternFeatureData::Group2PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.html)
[IChainPatternFeatureData::Group2PatternComponent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PatternComponent.html)
[IChainPatternFeatureData::ClearGroup2Selections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ClearGroup2Selections.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
