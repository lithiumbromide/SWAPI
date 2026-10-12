---
title: "GetRelations Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "GetRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelations.html"
---

# GetRelations Method (ISketchRelationManager)

Gets all of the sketch relations in the sketch based on the specified filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelations( _
   ByVal Filter As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim Filter As System.Integer
Dim value As System.Object

value = instance.GetRelations(Filter)
```

### C#

```csharp
System.object GetRelations(
   System.int Filter
)
```

### C++/CLI

```cpp
System.Object^ GetRelations(
   System.int Filter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Filter`: Sketch relation as defined in [swSketchRelationFilterType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationFilterType_e.html)

### Return Value

Array of [sketch relations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html)

## VBA Syntax

See [SketchRelationManager::GetRelations](ms-its:sldworksapivb6.chm::/sldworks~SketchRelationManager~GetRelations.html).

## Examples

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## Remarks

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate on any dynamically allocated memory.

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::IGetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetRelations.html)
[ISketchRelationManager::GetRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelationsCount.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
