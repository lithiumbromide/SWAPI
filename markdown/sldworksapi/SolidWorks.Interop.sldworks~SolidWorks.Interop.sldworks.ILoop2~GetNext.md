---
title: "GetNext Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.html"
---

# GetNext Method (ILoop2)

Gets the next loop on the face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As System.Object

value = instance.GetNext()
```

### C#

```csharp
System.object GetNext()
```

### C++/CLI

```cpp
System.Object^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) in face, or null or nothing if it is the last loop

## VBA Syntax

See [Loop2::GetNext](ms-its:sldworksapivb6.chm::/sldworks~Loop2~GetNext.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Get Loops (VBA)](Get_Loops_Example_VB.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
