---
title: "GetSense Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "GetSense"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetSense.html"
---

# GetSense Method (ICoEdge)

Gets the sense of the coedge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSense() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As System.Boolean

value = instance.GetSense()
```

### C#

```csharp
System.bool GetSense()
```

### C++/CLI

```cpp
System.bool GetSense();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the coedge has the same direction as the underlying edge, false if not

## VBA Syntax

See [CoEdge::GetSense](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~GetSense.html).

## Examples

[Select Tangent Edges via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)
[Get Sense for Each Coedge in a Loop (VBA)](Get_Sense_for_Each_Coedge_in_a_Loop_Example_VB.htm)

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
