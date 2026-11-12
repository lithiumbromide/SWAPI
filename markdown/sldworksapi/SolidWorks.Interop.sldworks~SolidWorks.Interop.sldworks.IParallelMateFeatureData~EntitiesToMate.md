---
title: "EntitiesToMate Property (IParallelMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IParallelMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IParallelMateFeatureData)

Gets or sets the entities to mate in this parallel mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IParallelMateFeatureData
Dim value As System.Object

instance.EntitiesToMate = value

value = instance.EntitiesToMate
```

### C#

```csharp
System.object EntitiesToMate {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Entities to mate (see **Remarks**)

## VBA Syntax

See [ParallelMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~ParallelMateFeatureData~EntitiesToMate.html).

## Examples

See the [IParallelMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.html) example.

## Remarks

You can create parallel mates with the following mate entity combinations:

| Mate entity/Mate entity | IRefAxis (cone, cylinder) | IFace2 (extrusion face, draft is not allowed) | IEdge , IRefAxis, ICenterLine , ISketchLine (line) | IRefPlane | ISurface , IFace2 (non-analytic surface) |
| --- | --- | --- | --- | --- | --- |
| IRefAxis (cone, cylinder) | ● | ● | ● |  | ● |
| IFace2 (extrusion face, draft is not allowed) | ● | ● | ● |  |  |
| IEdge, IRefAxis, ICenterLine, ISketchLine (line) | ● | ● | ● | ● | ● |
| IRefPlane |  |  | ● | ● |  |
| ISurface, IFace2 (non-analytic surface) | ● |  | ● |  |  |

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[IParallelMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.html)
[IParallelMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
