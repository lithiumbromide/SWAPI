---
title: "PropagatingEdges Property (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "PropagatingEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~PropagatingEdges.html"
---

# PropagatingEdges Property (ISurfaceExtendFeatureData)

Gets or sets the propagating edges for this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagatingEdges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
Dim value As System.Object

instance.PropagatingEdges = value

value = instance.PropagatingEdges
```

### C#

```csharp
System.object PropagatingEdges {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PropagatingEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of propagating [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [SurfaceExtendFeatureData::PropagatingEdges](ms-its:sldworksapivb6.chm::/sldworks~SurfaceExtendFeatureData~PropagatingEdges.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::GetPropagatingEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~GetPropagatingEdgesCount.html)
[ISurfaceExtendFeatureData::IGetPropagatingEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IGetPropagatingEdges.html)
[ISurfaceExtendFeatureData::ISetPropagatingEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~ISetPropagatingEdges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
