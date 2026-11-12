---
title: "GetBody Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetBody.html"
---

# GetBody Method (IEdge)

Gets the body for this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As Body2

value = instance.GetBody()
```

### C#

```csharp
Body2 GetBody()
```

### C++/CLI

```cpp
Body2^ GetBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object for this edge

## VBA Syntax

See [Edge::GetBody](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetBody.html).

## Examples

[Extend Surface (VBA)](Extend_Surface_Example_VB.htm)
[Create Temporary Bodies by Offsetting Surface Body (C#)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_CSharp.htm)
[Create Temporary Bodies by Offsetting Surface Body (VB.NET)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VBNET.htm)
[Create Temporary Bodies by Offsetting Surface Body (VBA)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VB.htm)

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
