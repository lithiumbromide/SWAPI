---
title: "PathPlaneReference Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "PathPlaneReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~PathPlaneReference.html"
---

# PathPlaneReference Property (IChainPatternFeatureData)

Gets or sets the reference plane for the [path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Path.html) selected for this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PathPlaneReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Object

instance.PathPlaneReference = value

value = instance.PathPlaneReference
```

### C#

```csharp
System.object PathPlaneReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PathPlaneReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [ChainPatternFeatureData::PathPlaneReference](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~PathPlaneReference.html).

## Remarks

This property is:

- only available when the path is a [sketch line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html).
- available for all types of chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
