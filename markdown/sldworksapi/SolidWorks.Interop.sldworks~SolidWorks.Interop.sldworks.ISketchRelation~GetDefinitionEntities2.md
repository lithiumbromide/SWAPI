---
title: "GetDefinitionEntities2 Method (ISketchRelation)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelation"
member: "GetDefinitionEntities2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetDefinitionEntities2.html"
---

# GetDefinitionEntities2 Method (ISketchRelation)

Gets the actual entities associated with this sketch relation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefinitionEntities2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelation
Dim value As System.Object

value = instance.GetDefinitionEntities2()
```

### C#

```csharp
System.object GetDefinitionEntities2()
```

### C++/CLI

```cpp
System.Object^ GetDefinitionEntities2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the actual entities for this sketch relation

## VBA Syntax

See [SketchRelation::GetDefinitionEntities2](ms-its:sldworksapivb6.chm::/sldworks~SketchRelation~GetDefinitionEntities2.html).

## Examples

[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## Remarks

When you create a sketch relation, an internal entity may be created to define that sketch relation. For example, if you add a sketch relation by specifying or selecting a point and an edge, a sketch segment may be created. If this happens, then [ISketchRelation::GetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~GetEntities.html) and [ISketchRelation::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetEntities.html) return the point and sketch segment.

To get the actual entities used to define the sketch relation, call ISketchRelation::GetDefinitionEntities2 or [ISketchRelation::IGetDefinitionEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation~IGetDefinitionEntities2.html). For example, if the relation is of type [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html).swConstraintType_OFFSETEDGE, and the relation is created by selecting a face, then this method returns that face.

Because some of the objects may be null, you should check for null before accessing them. You should deallocate any dynamically allocated memory.

## See Also

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.html)
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html)
[ISketchRelation::GetEntitiesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
