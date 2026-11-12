---
title: "GetNext Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetNext.html"
---

# GetNext Method (ICoEdge)

Gets the next coedge from the current coedge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
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

Coedge from the current coedge

## VBA Syntax

See [CoEdge::GetNext](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~GetNext.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Select Tangent Edges via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)

## Remarks

This method is cyclical; it loops back on itself and does not return NULL.

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetNext.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)
[ILoop2::GetCoEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdgeCount.html)
[ILoop2::GetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdges.html)
[ILoop2::IGetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetCoEdges.html)
