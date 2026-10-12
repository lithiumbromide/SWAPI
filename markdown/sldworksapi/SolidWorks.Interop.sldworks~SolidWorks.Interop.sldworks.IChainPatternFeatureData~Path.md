---
title: "Path Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Path"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Path.html"
---

# Path Property (IChainPatternFeatureData)

Gets or sets the path for this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Path As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Object

instance.Path = value

value = instance.Path
```

### C#

```csharp
System.object Path {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Path {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path:

- 2D or 3D [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html) containing an open or closed loop,
- Line in a sketch, or
- Model [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

## VBA Syntax

See [ChainPatternFeatureData::Path](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Path.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ReverseDirection.html)
[IChainPatternFeatureData::PathPlaneReference Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~PathPlaneReference.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
