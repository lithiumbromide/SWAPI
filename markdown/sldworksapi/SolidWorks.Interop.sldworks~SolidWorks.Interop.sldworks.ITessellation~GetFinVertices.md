---
title: "GetFinVertices Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetFinVertices"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinVertices.html"
---

# GetFinVertices Method (ITessellation)

Gets the IDs of the two vertices that correspond to a fin.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFinVertices( _
   ByVal FinId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As System.Object

value = instance.GetFinVertices(FinId)
```

### C#

```csharp
System.object GetFinVertices(
   System.int FinId
)
```

### C++/CLI

```cpp
System.Object^ GetFinVertices(
   System.int FinId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FinId`: Fin ID of the fin from which you want to return the vertices IDs

### Return Value

Array of two longs or two integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) describing the vertices IDs of a fin

## VBA Syntax

See [Tessellation::GetFinVertices](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetFinVertices.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetFinVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinVertices.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
