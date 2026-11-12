---
title: "GetDefinitionEntities Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "GetDefinitionEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetDefinitionEntities.html"
---

# GetDefinitionEntities Method (ISketchRelation)

Obsolete. Superseded by [ISketchRelation::GetDefinitionEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetDefinitionEntities2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefinitionEntities() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim value As System.Object

value = instance.GetDefinitionEntities()
```

### C#

```csharp
System.object GetDefinitionEntities()
```

### C++/CLI

```cpp
System.Object^ GetDefinitionEntities();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the actual entities for this sketch relation

## VBA Syntax

See [SketchRelation::GetDefinitionEntities](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~GetDefinitionEntities.html).

## Remarks

When you created a sketch relation, an internal entity may have also been created to define that sketch relation. For example, if you added a sketch relation by specifying or selecting a point and an edge, a sketch segment may have been created. If this happened, then [ISketchRelation::GetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetEntities.html) and [ISketchRelation::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetEntities.html) would return the point and sketch segment. To get the actual entities used to define the sketch relation, call ISketchRelation::GetDefinitionEntities or [ISketchRelation::IGetDefinitionEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetDefinitionEntities.html).

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate any dynamically allocated memory.

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)
[ISketchRelation::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
