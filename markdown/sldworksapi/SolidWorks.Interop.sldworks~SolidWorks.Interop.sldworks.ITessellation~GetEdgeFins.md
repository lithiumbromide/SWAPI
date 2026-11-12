---
title: "GetEdgeFins Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetEdgeFins"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetEdgeFins.html"
---

# GetEdgeFins Method (ITessellation)

Gets all of the fin IDs corresponding to a edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeFins( _
   ByVal EdgeDisp As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim EdgeDisp As System.Object
Dim value As System.Object

value = instance.GetEdgeFins(EdgeDisp)
```

### C#

```csharp
System.object GetEdgeFins(
   System.object EdgeDisp
)
```

### C++/CLI

```cpp
System.Object^ GetEdgeFins(
   System.Object^ EdgeDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeDisp`: [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) object

### Return Value

Array of long or integer values describing the unique fin ID of every fin shared by this edge

## VBA Syntax

See [Tessellation::GetEdgeFins](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetEdgeFins.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetEdgeFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetEdgeFins.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
