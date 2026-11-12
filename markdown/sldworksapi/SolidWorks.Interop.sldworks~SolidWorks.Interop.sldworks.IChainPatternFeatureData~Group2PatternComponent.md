---
title: "Group2PatternComponent Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Group2PatternComponent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PatternComponent.html"
---

# Group2PatternComponent Property (IChainPatternFeatureData)

Gets or sets the component to pattern for **Chain Group 2** in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Group2PatternComponent As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Object

instance.Group2PatternComponent = value

value = instance.Group2PatternComponent
```

### C#

```csharp
System.object Group2PatternComponent {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Group2PatternComponent {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) to pattern

## VBA Syntax

See [ChainPatternFeatureData::Group2PatternComponent](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Group2PatternComponent.html).

## Remarks

This property is only available to connected linkage chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::Group2FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2FlipPlane.html)
[IChainPatternFeatureData::Group2PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink1.html)
[IChainPatternFeatureData::Group2PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink2.html)
[IChainPatternFeatureData::Group2PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.html)
[IChainPatternFeatureData::ClearGroup2Selections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ClearGroup2Selections.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
