---
title: "GetFirstCoEdge Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "GetFirstCoEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html"
---

# GetFirstCoEdge Method (ILoop2)

Gets the first coedge of the loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstCoEdge() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As System.Object

value = instance.GetFirstCoEdge()
```

### C#

```csharp
System.object GetFirstCoEdge()
```

### C++/CLI

```cpp
System.Object^ GetFirstCoEdge();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [coedge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html) in loop

## VBA Syntax

See [Loop2::GetFirstCoEdge](ms-its:sldworksapivb6.chm::/sldworks~Loop2~GetFirstCoEdge.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## Remarks

The [ICoEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html) objects are returned in a CW or CCW manner based on the direction of the [ILoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see [ILoop2::IsOuter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IsOuter.html).

The coedge direction always aligns with the direction of the loop.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::EnumCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumCoEdges.html)
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)
[ILoop2::GetCoEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdgeCount.html)
[ILoop2::GetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdges.html)
[ILoop2::IGetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetCoEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
