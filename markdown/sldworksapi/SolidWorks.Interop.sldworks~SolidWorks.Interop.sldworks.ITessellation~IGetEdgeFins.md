---
title: "IGetEdgeFins Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetEdgeFins"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetEdgeFins.html"
---

# IGetEdgeFins Method (ITessellation)

Gets all of the fin IDs corresponding to a edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdgeFins( _
   ByVal EdgeObj As Edge _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim EdgeObj As Edge
Dim value As System.Integer

value = instance.IGetEdgeFins(EdgeObj)
```

### C#

```csharp
System.int IGetEdgeFins(
   Edge EdgeObj
)
```

### C++/CLI

```cpp
System.int IGetEdgeFins(
   Edge^ EdgeObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeObj`: [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) object

### Return Value

- in-process, unmanaged C++: Pointer to an array of long or integer values describing the unique fin ID of every fin shared by this edge

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::GetEdgeFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetEdgeFins.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
