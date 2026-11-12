---
title: "Group2PathLink2 Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Group2PathLink2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink2.html"
---

# Group2PathLink2 Property (IChainPatternFeatureData)

Gets or sets **Path Link 2** in **Chain Group 2** in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Group2PathLink2 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Object

instance.Group2PathLink2 = value

value = instance.Group2PathLink2
```

### C#

```csharp
System.object Group2PathLink2 {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Group2PathLink2 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

**Path Link 2** in **Chain Group 2**:

- Cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html),
- Circular or linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html),
- [Sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html),
- [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), or
- [Reference axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)

## VBA Syntax

See [ChainPatternFeatureData::Group2PathLink2](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Group2PathLink2.html).

## Remarks

This property is only available for connected linkage chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::Group2FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2FlipPlane.html)
[IChainPatternFeatureData::Group2PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink1.html)
[IChainPatternFeatureData::Group2PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.html)
[IChainPatternFeatureData::Group2PatternComponent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PatternComponent.html)
[IChainPatternFeatureData::ClearGroup2Selections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ClearGroup2Selections.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
