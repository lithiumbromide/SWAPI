---
title: "GetRelationsCount Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "GetRelationsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelationsCount.html"
---

# GetRelationsCount Method (ISketchRelationManager)

Gets the number of sketch relations in the sketch based on the specified filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelationsCount( _
   ByVal Filter As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim Filter As System.Integer
Dim value As System.Integer

value = instance.GetRelationsCount(Filter)
```

### C#

```csharp
System.int GetRelationsCount(
   System.int Filter
)
```

### C++/CLI

```cpp
System.int GetRelationsCount(
   System.int Filter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Filter`: Sketch relation as defined in [swSketchRelationFilterType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationFilterType_e.html)

### Return Value

Number of sketch relations

## VBA Syntax

See [SketchRelationManager::GetRelationsCount](ms-its:sldworksapivb6.chm::/sldworks~SketchRelationManager~GetRelationsCount.html).

## Examples

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)

## Remarks

Call this method before calling [ISketchRelationManager::IAddRelation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelationManager~IAddRelation.html) and [ISketchRelationManager::IGetRelations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelationManager~IGetRelations.html) to get the size of the array for that method.

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::AddRelation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~AddRelation.html)
[ISketchRelationManager::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
