---
title: "GetEdges Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "GetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdges.html"
---

# GetEdges Method (ILoop2)

Gets all the edges in the loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As System.Object

value = instance.GetEdges()
```

### C#

```csharp
System.object GetEdges()
```

### C++/CLI

```cpp
System.Object^ GetEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) that make up the loop

## VBA Syntax

See [Loop2::GetEdges](ms-its:sldworksapivb6.chm::/sldworks~Loop2~GetEdges.html).

## Examples

[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## Remarks

The [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) objects are returned in a clockwise (CW) or counter-clockwise (CCW) manner based on the direction of the [ILoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, use [ILoop2::IsOuter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IsOuter.html).

Because an edge is shared by multiple loops, the edge direction might be opposite to the direction of the ILoop2. To check this, use [IEdge::EdgeInFaceSense](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~EdgeInFaceSense.html).

If the loop is a singular loop, use [ILoop2::GetVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~GetVertices.html) to get its position (a single vertex). ILoop2::GetEdges returns an empty array if the loop is singular.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdgeCount.html)
[ILoop2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetEdges.html)
[ILoop2::EnumEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
