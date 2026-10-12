---
title: "GetFacetCount Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetFacetCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetCount.html"
---

# GetFacetCount Method (ITessellation)

Gets the number of facets used to create this tessellation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacetCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Integer

value = instance.GetFacetCount()
```

### C#

```csharp
System.int GetFacetCount()
```

### C++/CLI

```cpp
System.int GetFacetCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of facets

## VBA Syntax

See [Tessellation::GetFacetCount](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetFacetCount.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
