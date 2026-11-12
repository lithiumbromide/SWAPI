---
title: "ISetEntities Method (ISurfaceOffsetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData"
member: "ISetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetEntities.html"
---

# ISetEntities Method (ISurfaceOffsetFeatureData)

Sets the offset surfaces or faces for this surface offset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEntities( _
   ByVal Count As System.Integer, _
   ByRef EntityArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceOffsetFeatureData
Dim Count As System.Integer
Dim EntityArray As System.Object

instance.ISetEntities(Count, EntityArray)
```

### C#

```csharp
void ISetEntities(
   System.int Count,
   ref System.object EntityArray
)
```

### C++/CLI

```cpp
void ISetEntities(
   System.int Count,
   System.Object^% EntityArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of offset surfaces or faces
- `EntityArray`: - in-process, unmanaged C++: Pointer to an array of offset surface or face feature [entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html)
[ISurfaceOffsetFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Entities.html)
[ISurfaceOffsetFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~IGetEntities.html)
[ISurfaceOffsetFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetEntitiesCount.html)

## Availability

SOLIDWORKS 2012 SP04, Revision Number 20.4
