---
title: "GetCoEdges Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "GetCoEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdges.html"
---

# GetCoEdges Method (ILoop2)

Gets the coedges in this loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As System.Object

value = instance.GetCoEdges()
```

### C#

```csharp
System.object GetCoEdges()
```

### C++/CLI

```cpp
System.Object^ GetCoEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [coedges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html)

## VBA Syntax

See [Loop2::GetCoEdges](ms-its:sldworksapivb6.chm::/sldworks~Loop2~GetCoEdges.html).

## Examples

[Get Sense for Each Coedge in a Loop (VBA)](Get_Sense_for_Each_Coedge_in_a_Loop_Example_VB.htm)

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetCoEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdgeCount.html)
[ILoop2::IGetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetCoEdges.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)
[ICoEdge::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetNext.html)
[ICoEdge::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetNext.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
