---
title: "IGetEdgeFinsCount Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetEdgeFinsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetEdgeFinsCount.html"
---

# IGetEdgeFinsCount Method (ITessellation)

Gets the number of fins corresponding to an edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdgeFinsCount( _
   ByVal EdgeObj As Edge _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim EdgeObj As Edge
Dim value As System.Integer

value = instance.IGetEdgeFinsCount(EdgeObj)
```

### C#

```csharp
System.int IGetEdgeFinsCount(
   Edge EdgeObj
)
```

### C++/CLI

```cpp
System.int IGetEdgeFinsCount(
   Edge^ EdgeObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeObj`: [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) object of which to get the number

### Return Value

Number of fins corresponding to the specified edge

## VBA Syntax

See [Tessellation::IGetEdgeFinsCount](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetEdgeFinsCount.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
