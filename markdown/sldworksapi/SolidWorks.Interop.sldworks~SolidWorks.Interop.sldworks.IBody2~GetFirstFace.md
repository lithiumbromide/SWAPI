---
title: "GetFirstFace Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetFirstFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.html"
---

# GetFirstFace Method (IBody2)

Finds the first face in a body and returns the face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetFirstFace()
```

### C#

```csharp
System.object GetFirstFace()
```

### C++/CLI

```cpp
System.Object^ GetFirstFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First face in the body

## VBA Syntax

See [Body2::GetFirstFace](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetFirstFace.html).

## Examples

[Get Part Bounding Box (VBA)](Get_Part_Bounding_Box_Example_VB.htm)
[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaceCount.html)
[IBody2::EnumFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~EnumFaces.html)
[IBody2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html)
[IBody2::DeleteBlends2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.html)
[IBody2::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaces.html)
[IBody2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
