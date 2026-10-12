---
title: "IGetDraftedEntities Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "IGetDraftedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetDraftedEntities.html"
---

# IGetDraftedEntities Method (IDraftFeatureData2)

Gets the drafted entities (faces or edges) for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDraftedEntities( _
   ByVal Count As System.Short _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim Count As System.Short
Dim value As Entity

value = instance.IGetDraftedEntities(Count)
```

### C#

```csharp
Entity IGetDraftedEntities(
   System.short Count
)
```

### C++/CLI

```cpp
Entity^ IGetDraftedEntities(
   System.short Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of [entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IDraftFeatureData2::GetDraftedEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~GetDraftedEntityCount.html) to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::GetDraftedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntities.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
