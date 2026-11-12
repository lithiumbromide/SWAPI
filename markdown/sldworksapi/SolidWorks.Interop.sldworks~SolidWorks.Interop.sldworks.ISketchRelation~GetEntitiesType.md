---
title: "GetEntitiesType Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "GetEntitiesType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesType.html"
---

# GetEntitiesType Method (ISketchRelation)

Gets the types of entities in this sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesType() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim value As System.Object

value = instance.GetEntitiesType()
```

### C#

```csharp
System.object GetEntitiesType()
```

### C++/CLI

```cpp
System.Object^ GetEntitiesType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of types of entities in this sketch relation as defined by [swSketchRelationEntityTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationEntityTypes_e.html)

## VBA Syntax

See [SketchRelation::GetEntitiesType](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~GetEntitiesType.html).

## Examples

[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)
[ISketchRelation::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntities.html)
[ISketchRelation::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
