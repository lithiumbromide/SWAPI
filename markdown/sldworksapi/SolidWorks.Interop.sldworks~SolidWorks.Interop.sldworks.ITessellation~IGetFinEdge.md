---
title: "IGetFinEdge Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFinEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinEdge.html"
---

# IGetFinEdge Method (ITessellation)

Gets the edge corresponding to a fin.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFinEdge( _
   ByVal FinId As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As Edge

value = instance.IGetFinEdge(FinId)
```

### C#

```csharp
Edge IGetFinEdge(
   System.int FinId
)
```

### C++/CLI

```cpp
Edge^ IGetFinEdge(
   System.int FinId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FinId`: ID of the fin from which you want to return the edge

### Return Value

[Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) with which this fin is shared

## VBA Syntax

See [Tessellation::IGetFinEdge](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetFinEdge.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0[ITessellate::GetFinEdge Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~GetFinEdge.html)
