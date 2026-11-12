---
title: "TranslateToVertex Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "TranslateToVertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TranslateToVertex.html"
---

# TranslateToVertex Property (IMoveCopyBodyFeatureData)

Gets or sets the entity to which to move the selected bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property TranslateToVertex As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Object

instance.TranslateToVertex = value

value = instance.TranslateToVertex
```

### C#

```csharp
System.object TranslateToVertex {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TranslateToVertex {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Coordinate system](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html), [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html), or [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) to which to move the selected bodies

## VBA Syntax

See [MoveCopyBodyFeatureData::TranslateToVertex](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~TranslateToVertex.html).

## Examples

[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)

## Remarks

A coordinate system, sketch point, or vertex must be selected from which to move the selected bodies.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
