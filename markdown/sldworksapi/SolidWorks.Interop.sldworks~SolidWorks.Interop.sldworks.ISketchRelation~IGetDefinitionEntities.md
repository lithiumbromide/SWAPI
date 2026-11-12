---
title: "IGetDefinitionEntities Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "IGetDefinitionEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetDefinitionEntities.html"
---

# IGetDefinitionEntities Method (ISketchRelation)

Obsolete. Superseded by [ISketchRelation::IGetDefinitionEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetDefinitionEntities2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDefinitionEntities( _
   ByVal NumEntities As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim NumEntities As System.Integer
Dim value As System.Object

value = instance.IGetDefinitionEntities(NumEntities)
```

### C#

```csharp
System.object IGetDefinitionEntities(
   System.int NumEntities
)
```

### C++/CLI

```cpp
System.Object^ IGetDefinitionEntities(
   System.int NumEntities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumEntities`: Number of actual entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of the actual entities for this sketch relation

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

When you created a sketch relation, an internal entity may have also been created to define that sketch relation. For example, if you added a sketch relation by specifying or selecting a point and an edge, a sketch segment may have been created. If this happened, then [ISketchRelation::GetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetEntities.html) and [ISketchRelation::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetEntities.html) would return the point and sketch segment. To get the actual entities used to define the sketch relation, call [ISketchRelation::GetDefinitionEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetDefinitionEntities.html) or ISketchRelation::IGetDefinitionEntities.

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate any dynamically allocated memory.

Before calling this method, call [ISketchRelation::GetEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetEntitiesCount.html) to get the value for NumEntities.

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
