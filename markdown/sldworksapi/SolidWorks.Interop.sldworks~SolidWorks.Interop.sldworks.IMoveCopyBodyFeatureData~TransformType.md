---
title: "TransformType Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "TransformType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.html"
---

# TransformType Property (IMoveCopyBodyFeatureData)

Gets or sets whether to move or rotate the selected bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransformType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Integer

instance.TransformType = value

value = instance.TransformType
```

### C#

```csharp
System.int TransformType {get; set;}
```

### C++/CLI

```cpp
property System.int TransformType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Move or rotate the selected bodies as defined in [swMoveCopyBodyFeatureTransformType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyBodyFeatureTransformType_e.html)

## VBA Syntax

See [MoveCopyBodyFeatureData::TransformType](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~TransformType.html).

## Examples

[Copy and Rotate Body Using Edge (VBA)](Copy_and_Rotate_Body_using_Edge_Example_VB.htm)
[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)

## Remarks

Use this property to get or set the transform type before setting any of these properties:

- [IMoveCopyBodyFeatureData::TransformX](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformX.html)
- [IMoveCopyBodyFeatureData::TransformY](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformY.html)
- [IMoveCopyBodyFeatureData::TransformZ](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformZ.html)

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
