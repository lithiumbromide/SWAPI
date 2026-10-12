---
title: "BoundingEntities Property (ISurfacePlanarFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfacePlanarFeatureData"
member: "BoundingEntities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~BoundingEntities.html"
---

# BoundingEntities Property (ISurfacePlanarFeatureData)

Gets or sets the bounding entities for this planar surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BoundingEntities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfacePlanarFeatureData
Dim value As System.Object

instance.BoundingEntities = value

value = instance.BoundingEntities
```

### C#

```csharp
System.object BoundingEntities {get; set;}
```

### C++/CLI

```cpp
property System.Object^ BoundingEntities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of bounding entities

## VBA Syntax

See [SurfacePlanarFeatureData::BoundingEntities](ms-its:sldworksapivb6.chm::/sldworks~SurfacePlanarFeatureData~BoundingEntities.html).

## Examples

See the [ISurfacePlanarFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html)
[ISurfacePlanarFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData_members.html)
[ISurfacePlanarSurfaceData::GetBoundingEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~GetBoundingEntitiesCount.html)
[ISurfacePlanarSurfaceData::IGetBoundingEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~IGetBoundingEntities.html)
[ISurfacePlanarSurfaceData::ISetBoundingEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~ISetBoundingEntities.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
