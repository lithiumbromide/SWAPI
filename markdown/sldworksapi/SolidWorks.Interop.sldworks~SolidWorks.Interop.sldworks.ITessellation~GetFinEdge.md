---
title: "GetFinEdge Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetFinEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinEdge.html"
---

# GetFinEdge Method (ITessellation)

Gets the edge corresponding to a fin.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFinEdge( _
   ByVal FinId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As System.Object

value = instance.GetFinEdge(FinId)
```

### C#

```csharp
System.object GetFinEdge(
   System.int FinId
)
```

### C++/CLI

```cpp
System.Object^ GetFinEdge(
   System.int FinId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FinId`: ID of the fin from which you want to return the edge

### Return Value

[Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) with which this fin is shared

## VBA Syntax

See [Tessellation::GetFinEdge](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetFinEdge.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetFinEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinEdge.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
