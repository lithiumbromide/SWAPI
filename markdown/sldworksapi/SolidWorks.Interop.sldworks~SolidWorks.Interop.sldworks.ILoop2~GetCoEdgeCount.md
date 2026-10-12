---
title: "GetCoEdgeCount Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "GetCoEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdgeCount.html"
---

# GetCoEdgeCount Method (ILoop2)

Gets the number of coedges in this loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoEdgeCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As System.Integer

value = instance.GetCoEdgeCount()
```

### C#

```csharp
System.int GetCoEdgeCount()
```

### C++/CLI

```cpp
System.int GetCoEdgeCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of coedges in this loop

## VBA Syntax

See [Loop2::GetCoEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~Loop2~GetCoEdgeCount.html).

## Examples

[Get Sense for Each Coedge in a Loop (VBA)](Get_Sense_for_Each_Coedge_in_a_Loop_Example_VB.htm)

## Remarks

Call this method before calling [ILoop2::IGetCoEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IGetCoEdges.html) to determine the size of the array for that method.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdges.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)
[ICoEdge::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetNext.html)
[ICoEdge::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetNext.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
