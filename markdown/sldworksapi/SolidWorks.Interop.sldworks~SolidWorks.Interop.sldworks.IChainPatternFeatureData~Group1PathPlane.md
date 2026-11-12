---
title: "Group1PathPlane Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Group1PathPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathPlane.html"
---

# Group1PathPlane Property (IChainPatternFeatureData)

Gets or sets the position of the [pattern component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PatternComponent.html) relative to the [path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Path.html) in **Chain Group 1** in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Group1PathPlane As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Object

instance.Group1PathPlane = value

value = instance.Group1PathPlane
```

### C#

```csharp
System.object Group1PathPlane {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Group1PathPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Component [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html) or planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See [ChainPatternFeatureData::Group1PathPlane](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Group1PathPlane.html).

## Remarks

This property is available for all types of chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::Group1FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1FlipPlane.html)
[IChainPatternFeatureData::Group1PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink1.html)
[IChainPatternFeatureData::Group1PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink2.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
