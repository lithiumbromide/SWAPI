---
title: "GetFacetEdges Method (IFacet)"
project: "SOLIDWORKS API Help"
interface: "IFacet"
member: "GetFacetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet~GetFacetEdges.html"
---

# GetFacetEdges Method (IFacet)

Gets the three edges of this facet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacetEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFacet
Dim value As System.Object

value = instance.GetFacetEdges()
```

### C#

```csharp
System.object GetFacetEdges()
```

### C++/CLI

```cpp
System.Object^ GetFacetEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of three [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)s

## VBA Syntax

See [Facet::GetFacetEdges](ms-its:sldworksapivb6.chm::/sldworks~Facet~GetFacetEdges.html).

## Examples

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html) examples.

## See Also

[IFacet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html)
[IFacet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
