---
title: "IGetEdges Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetEdges.html"
---

# IGetEdges Method (IBody2)

Gets the edges for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdges( _
   ByVal Count As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Count As System.Integer
Dim value As Edge

value = instance.IGetEdges(Count)
```

### C#

```csharp
Edge IGetEdges(
   System.int Count
)
```

### C++/CLI

```cpp
Edge^ IGetEdges(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBody2::GetEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetEdgeCount.html) to determine the size of the array.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetEdges.html)
[IModelDocExtenstion::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
