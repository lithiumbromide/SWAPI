---
title: "IGetEntitiesType Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "IGetEntitiesType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntitiesType.html"
---

# IGetEntitiesType Method (ISketchRelation)

Gets the types of entities in this sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntitiesType( _
   ByVal NumEntities As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim NumEntities As System.Integer
Dim value As System.Integer

value = instance.IGetEntitiesType(NumEntities)
```

### C#

```csharp
System.int IGetEntitiesType(
   System.int NumEntities
)
```

### C++/CLI

```cpp
System.int IGetEntitiesType(
   System.int NumEntities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumEntities`: Number of entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of types of entities in this sketch relation as defined by [swSketchRelationEntityTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationEntityTypes_e.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchRelation::GetEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetEntitiesCount.html) to get the value for NumEntities.

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)
[ISketchRelation::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntities.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
