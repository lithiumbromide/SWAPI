---
title: "GetFirstLoop Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetFirstLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.html"
---

# GetFirstLoop Method (IFace2)

Gets the first loop in this face, which is not necessarily the outer loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstLoop() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetFirstLoop()
```

### C#

```csharp
System.object GetFirstLoop()
```

### C++/CLI

```cpp
System.Object^ GetFirstLoop();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html)

## VBA Syntax

See [Face2::GetFirstLoop](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetFirstLoop.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Get Loops (VBA)](Get_Loops_Example_VB.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)
[Sweep Planar Loop Along Vector (VBA)](Sweep_Planar_Loop_Along_Vector_Example_VB.htm)
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.html)
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.html)
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.html)
[ILoop2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
