---
title: "GetVertexCount Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetVertexCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexCount.html"
---

# GetVertexCount Method (ITessellation)

Gets the number of vertices for this tessellation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertexCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Integer

value = instance.GetVertexCount()
```

### C#

```csharp
System.int GetVertexCount()
```

### C++/CLI

```cpp
System.int GetVertexCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of vertices for this tessellation

## VBA Syntax

See [Tessellation::GetVertexCount](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetVertexCount.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
