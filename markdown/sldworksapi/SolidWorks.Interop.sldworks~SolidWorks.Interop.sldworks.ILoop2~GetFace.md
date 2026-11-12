---
title: "GetFace Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "GetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFace.html"
---

# GetFace Method (ILoop2)

Gets the face containing this loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As System.Object

value = instance.GetFace()
```

### C#

```csharp
System.object GetFace()
```

### C++/CLI

```cpp
System.Object^ GetFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Loop2::GetFace](ms-its:sldworksapivb6.chm::/sldworks~Loop2~GetFace.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::IGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
