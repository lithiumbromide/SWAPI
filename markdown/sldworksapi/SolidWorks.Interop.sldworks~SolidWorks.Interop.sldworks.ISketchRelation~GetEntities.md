---
title: "GetEntities Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "GetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntities.html"
---

# GetEntities Method (ISketchRelation)

Gets the entities associated with this sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntities() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim value As System.Object

value = instance.GetEntities()
```

### C#

```csharp
System.object GetEntities()
```

### C++/CLI

```cpp
System.Object^ GetEntities();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of entities for this sketch relation

## VBA Syntax

See [SketchRelation::GetEntities](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~GetEntities.html).

## Examples

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## Remarks

When you create a sketch relation, an internal entity may also be created to define that sketch relation. For example, if you add a sketch relation by specifying or selecting a point and an edge, a sketch segment may be created. If this happens, then ISketchRelation::GetEntities and [ISketchRelation::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetEntities.html) return the point and sketch segment. To get the actual entities used to define the sketch relation, call [ISketchRelation::GetDefinitionEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetDefinitionEntities.html) or [ISketchRelation::IGetDefinitionEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetDefinitionEntities.html).

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate any dynamically allocated memory.

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)
[ISketchRelation::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
