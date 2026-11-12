---
title: "GetEntitiesCount Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "GetEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.html"
---

# GetEntitiesCount Method (ISketchRelation)

Gets the number of entities associated with this sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim value As System.Integer

value = instance.GetEntitiesCount()
```

### C#

```csharp
System.int GetEntitiesCount()
```

### C++/CLI

```cpp
System.int GetEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities for this sketch relation

## VBA Syntax

See [SketchRelation::GetEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~GetEntitiesCount.html).

## Examples

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)

## Remarks

Call this method before calling [ISketchRelation::IGetDefinitionEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetDefinitionEntities.html), [ISketchRelation::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetEntities.html), or [ISketchRelation::IGetEntitiesType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetEntitiesType.html) to determine the size of array for the entities or types of entities associated with the sketch relation.

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
