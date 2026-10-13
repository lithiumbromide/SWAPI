---
title: "RemoveRedundantTopology Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "RemoveRedundantTopology"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveRedundantTopology.html"
---

# RemoveRedundantTopology Method (IEdge)

Removes redundant topology from the edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveRedundantTopology() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Boolean

value = instance.RemoveRedundantTopology()
```

### C#

```csharp
System.bool RemoveRedundantTopology()
```

### C++/CLI

```cpp
System.bool RemoveRedundantTopology();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if redundant topology was removed successfully, false if not

## VBA Syntax

See [Edge::RemoveRedundantTopology](ms-its:sldworksapivb6.chm::/sldworks~Edge~RemoveRedundantTopology.html).

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
