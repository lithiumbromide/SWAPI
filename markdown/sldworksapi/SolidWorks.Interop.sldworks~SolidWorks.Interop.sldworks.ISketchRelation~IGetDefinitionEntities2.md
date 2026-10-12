---
title: "IGetDefinitionEntities2 Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "IGetDefinitionEntities2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetDefinitionEntities2.html"
---

# IGetDefinitionEntities2 Method (ISketchRelation)

Gets the actual entities associated with this sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDefinitionEntities2( _
   ByVal NumEntities As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim NumEntities As System.Integer
Dim value As System.Object

value = instance.IGetDefinitionEntities2(NumEntities)
```

### C#

```csharp
System.object IGetDefinitionEntities2(
   System.int NumEntities
)
```

### C++/CLI

```cpp
System.Object^ IGetDefinitionEntities2(
   System.int NumEntities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumEntities`: Number of actual entities

### Return Value

- In-process, unmanaged C++: Pointer to an array of the actual entities for this sketch relation

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

When you create a sketch relation, an internal entity may also be created to define that sketch relation. For example, if you add a sketch relation by specifying or selecting a point and an edge, a sketch segment may be created. If this happens, then [ISketchRelation::GetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetEntities.html) and [ISketchRelation::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetEntities.html) return the point and sketch segment.

To get the actual entities used to define the sketch relation, call [ISketchRelation::GetDefinitionEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetDefinitionEntities2.html) or ISketchRelation::IGetDefinitionEntities2. For example, if the relation is of type [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html).swConstraintType_OFFSETEDGE, and the relation is created by selecting a face, then this method returns that face.

Because some of the objects may be null, you should check for null before accessing them. You should deallocate any dynamically allocated memory.

Before calling this method, call [ISketchRelation::GetEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetEntitiesCount.html) to get the value for NumEntities.

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
