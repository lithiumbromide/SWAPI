---
title: "TransformReferenceEntity Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "TransformReferenceEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.html"
---

# TransformReferenceEntity Property (IMoveCopyBodyFeatureData)

Gets or sets the entity to reference when moving or rotating the selected bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransformReferenceEntity As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Object

instance.TransformReferenceEntity = value

value = instance.TransformReferenceEntity
```

### C#

```csharp
System.object TransformReferenceEntity {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TransformReferenceEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to one of these entities:

- [Coordinate system](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- [Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- [Sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)
- [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [MoveCopyBodyFeatureData::TransformReferenceEntity](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~TransformReferenceEntity.html).

## Examples

[Copy and Rotate Body Using Edge (VBA)](Copy_and_Rotate_Body_using_Edge_Example_VB.htm)
[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
