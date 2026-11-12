---
title: "IGetCoEdges Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IGetCoEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetCoEdges.html"
---

# IGetCoEdges Method (ILoop2)

Gets the coedges in this loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCoEdges( _
   ByVal NumCoEdges As System.Integer _
) As CoEdge
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim NumCoEdges As System.Integer
Dim value As CoEdge

value = instance.IGetCoEdges(NumCoEdges)
```

### C#

```csharp
CoEdge IGetCoEdges(
   System.int NumCoEdges
)
```

### C++/CLI

```cpp
CoEdge^ IGetCoEdges(
   System.int NumCoEdges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumCoEdges`: Number of coedges in this loop

### Return Value

- in-process, unmanaged C++: Pointer to an array of [coedges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ILoop2::GetCoEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~GetCoEdgeCount.html) to get NumCoEdges.

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
