---
title: "Highlight Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "Highlight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight.html"
---

# Highlight Method (IEdge)

Add highlights or removes highlights from this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Highlight( _
   ByVal State As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim State As System.Boolean

instance.Highlight(State)
```

### C#

```csharp
void Highlight(
   System.bool State
)
```

### C++/CLI

```cpp
void Highlight(
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`: True adds highlights to this edge, false removes highlights from this edge

## VBA Syntax

See [Edge::Highlight](ms-its:sldworksapivb6.chm::/sldworks~Edge~Highlight.html).

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::Display Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Display.html)
[IFace2::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight.html)
[IFace2::IHighlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight.html)
[IVertex::Display Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~Display.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
