---
title: "TransformX Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "TransformX"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformX.html"
---

# TransformX Property (IMoveCopyBodyFeatureData)

Gets or sets the x coordinate for either moving or rotating the selected bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransformX As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double

instance.TransformX = value

value = instance.TransformX
```

### C#

```csharp
System.double TransformX {get; set;}
```

### C++/CLI

```cpp
property System.double TransformX {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

x coordinate in meters for moving or radians for rotating

## VBA Syntax

See [MoveCopyBodyFeatureData::TransformX](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~TransformX.html).

## Examples

[Copy and Rotate Body Using Edge (VBA)](Copy_and_Rotate_Body_using_Edge_Example_VB.htm)
[Move and Copy Body By Setting Transforms (VBA)](Move_and_Copy_Body_by_Setting_Transforms_Example_VB.htm)
[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)

## Remarks

Use [IMoveCopyBodyFeatureData::TransformType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.html) to get or set the transform type before setting this property.

[IMoveCopyBodyFeatureData::TransformReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.html) must be:

- Nothing or null if moving the selected bodies.
  - or -
- a vertex if rotating the selected bodies.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)
[IMoveCopyBodyFeatureData::TransformY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformY.html)
[IMoveCopyBodyFeatureData::TransformZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformZ.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
