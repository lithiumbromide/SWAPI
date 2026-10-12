---
title: "GetFacets Method (IMeshBody)"
project: "SOLIDWORKS API Help"
interface: "IMeshBody"
member: "GetFacets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeshBody~GetFacets.html"
---

# GetFacets Method (IMeshBody)

Gets the facets on this mesh body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacets() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMeshBody
Dim value As System.Object

value = instance.GetFacets()
```

### C#

```csharp
System.object GetFacets()
```

### C++/CLI

```cpp
System.Object^ GetFacets();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html)s

## VBA Syntax

See [MeshBody::GetFacets](ms-its:sldworksapivb6.chm::/sldworks~MeshBody~GetFacets.html).

## Examples

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html) examples.

## See Also

[IMeshBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeshBody.html)
[IMeshBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeshBody_members.html)
[IMeshBody::GetFacetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeshBody~GetFacetCount.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
