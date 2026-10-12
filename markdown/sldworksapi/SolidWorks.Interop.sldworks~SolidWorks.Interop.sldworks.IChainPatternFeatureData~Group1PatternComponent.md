---
title: "Group1PatternComponent Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Group1PatternComponent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PatternComponent.html"
---

# Group1PatternComponent Property (IChainPatternFeatureData)

Gets or sets the component to pattern for **Chain Group 1** in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Group1PatternComponent As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Object

instance.Group1PatternComponent = value

value = instance.Group1PatternComponent
```

### C#

```csharp
System.object Group1PatternComponent {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Group1PatternComponent {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) to pattern

## VBA Syntax

See [ChainPatternFeatureData::Group1PatternComponent](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Group1PatternComponent.html).

## Remarks

This property is available to all types of chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::Group1FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1FlipPlane.html)
[IChainPatternFeatureData::Group1PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink1.html)
[IChainPatternFeatureData::Group1PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink2.html)
[IChainPatternFeatureData::Group1PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathPlane.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
