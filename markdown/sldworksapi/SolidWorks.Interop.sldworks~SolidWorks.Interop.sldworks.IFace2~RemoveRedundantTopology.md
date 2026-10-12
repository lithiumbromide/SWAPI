---
title: "RemoveRedundantTopology Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "RemoveRedundantTopology"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveRedundantTopology.html"
---

# RemoveRedundantTopology Method (IFace2)

Removes redundant topology from the face.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveRedundantTopology() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
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

True if the redundant topology was removed, false if not

## VBA Syntax

See [Face2::RemoveRedundantTopology](ms-its:sldworksapivb6.chm::/sldworks~Face2~RemoveRedundantTopology.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IEdge::RemoveRedundantTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveRedundantTopology.html)
[IBody2::RemoveRedundantTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveRedundantTopology.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
