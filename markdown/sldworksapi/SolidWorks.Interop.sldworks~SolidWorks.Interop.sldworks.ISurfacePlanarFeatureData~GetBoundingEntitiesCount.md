---
title: "GetBoundingEntitiesCount Method (ISurfacePlanarFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfacePlanarFeatureData"
member: "GetBoundingEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~GetBoundingEntitiesCount.html"
---

# GetBoundingEntitiesCount Method (ISurfacePlanarFeatureData)

Gets the number of bounding entities for this planar surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBoundingEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfacePlanarFeatureData
Dim value As System.Integer

value = instance.GetBoundingEntitiesCount()
```

### C#

```csharp
System.int GetBoundingEntitiesCount()
```

### C++/CLI

```cpp
System.int GetBoundingEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bounding entities

## VBA Syntax

See [SurfacePlanarFeatureData::GetBoundingEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~SurfacePlanarFeatureData~GetBoundingEntitiesCount.html).

## Examples

See the [ISurfacePlanarFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html) examples.

## Remarks

Call this method before calling [ISurfacePlanarFeatureData::IGetBoundingEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfacePlanarFeatureData~IGetBoundingEntities.html) to get the size of the array for that method.

## See Also

[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html)
[ISurfacePlanarFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData_members.html)
[ISurfacePlanarFeatureData::ISetBoundingEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~ISetBoundingEntities.html)
[ISurfacePlanarFeatureData::BoundingEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~BoundingEntities.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
