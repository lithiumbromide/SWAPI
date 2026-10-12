---
title: "Group1PathLink1 Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Group1PathLink1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink1.html"
---

# Group1PathLink1 Property (IChainPatternFeatureData)

Gets or sets **Path Link 1** in **Chain Group 1** in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Group1PathLink1 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Object

instance.Group1PathLink1 = value

value = instance.Group1PathLink1
```

### C#

```csharp
System.object Group1PathLink1 {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Group1PathLink1 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

**Path Link 1** in **Chain Group 1**:

- Cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html),
- Circular or linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html),
- [Sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html),
- [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), or
- [Reference axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)

## VBA Syntax

See [ChainPatternFeatureData::Group1PathLink1](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Group1PathLink1.html).

## Remarks

This property is available for all types of chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::Group1FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1FlipPlane.html)
[IChainPatternFeatureData::Group1PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink2.html)
[IChainPatternFeatureData::Group1PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathPlane.html)
[IChainPatternFeatureData::Group1PatternComponent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PatternComponent.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
