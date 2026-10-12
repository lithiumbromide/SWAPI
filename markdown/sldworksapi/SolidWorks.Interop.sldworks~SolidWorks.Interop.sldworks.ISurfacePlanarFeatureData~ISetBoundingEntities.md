---
title: "ISetBoundingEntities Method (ISurfacePlanarFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfacePlanarFeatureData"
member: "ISetBoundingEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~ISetBoundingEntities.html"
---

# ISetBoundingEntities Method (ISurfacePlanarFeatureData)

Sets the bounding entities for this planar surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetBoundingEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfacePlanarFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.ISetBoundingEntities(Count)
```

### C#

```csharp
System.object ISetBoundingEntities(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ ISetBoundingEntities(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bounding entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of bounding entities of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html)
[ISurfacePlanarFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData_members.html)
[ISurfacePlanarFeatureData::GetBoundingEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~GetBoundingEntitiesCount.html)
[ISurfacePlanarFeatureData::IGetBoundingEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~IGetBoundingEntities.html)
[ISurfacePlanarFeatureData::BoundingEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~BoundingEntities.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
