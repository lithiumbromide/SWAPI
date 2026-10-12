---
title: "IGetRelations Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "IGetRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetRelations.html"
---

# IGetRelations Method (ISketchRelationManager)

Gets all of the sketch relations in the sketch based on the specified filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRelations( _
   ByVal Filter As System.Integer, _
   ByVal Count As System.Integer _
) As SketchRelation
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim Filter As System.Integer
Dim Count As System.Integer
Dim value As SketchRelation

value = instance.IGetRelations(Filter, Count)
```

### C#

```csharp
SketchRelation IGetRelations(
   System.int Filter,
   System.int Count
)
```

### C++/CLI

```cpp
SketchRelation^ IGetRelations(
   System.int Filter,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Filter`: Sketch relation as defined in [swSketchRelationFilterType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationFilterType_e.html)
- `Count`: Number of sketch relations

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch relations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate on any dynamically allocated memory.

Call [ISketchRelationManager::GetRelationsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelationManager~GetRelationsCount.html) before calling this method to get the value for Count.

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
