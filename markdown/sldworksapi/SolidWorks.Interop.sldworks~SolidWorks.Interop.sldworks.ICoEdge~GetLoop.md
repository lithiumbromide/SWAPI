---
title: "GetLoop Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "GetLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetLoop.html"
---

# GetLoop Method (ICoEdge)

Gets the loop containing this coedge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLoop() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As System.Object

value = instance.GetLoop()
```

### C#

```csharp
System.object GetLoop()
```

### C++/CLI

```cpp
System.Object^ GetLoop();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Loop containing this coedge

## VBA Syntax

See [CoEdge::GetLoop](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~GetLoop.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::IGetLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetLoop2.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)
