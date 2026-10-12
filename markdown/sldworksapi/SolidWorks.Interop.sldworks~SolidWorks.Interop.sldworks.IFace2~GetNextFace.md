---
title: "GetNextFace Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetNextFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetNextFace.html"
---

# GetNextFace Method (IFace2)

Gets the next face in a body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetNextFace()
```

### C#

```csharp
System.object GetNextFace()
```

### C++/CLI

```cpp
System.Object^ GetNextFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) in a body

## VBA Syntax

See [Face2::GetNextFace](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetNextFace.html).

## Examples

[Get Part Bounding Box (VBA)](Get_Part_Bounding_Box_Example_VB.htm)
[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)
[Get Part Bounding Box (VBA)](Get_Part_Bounding_Box_Example_VB.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IBody2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.html)
[IBody2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html)
[IBody2::IGetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstSelectedFace.html)
[IBody2::GetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstSelectedFace.html)
[IFace2::IGetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetNextFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
