---
title: "IHighlight Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IHighlight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight.html"
---

# IHighlight Method (IFace2)

Adds highlighting to or removes highlighting from a face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IHighlight( _
   ByVal State As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim State As System.Boolean

instance.IHighlight(State)
```

### C#

```csharp
void IHighlight(
   System.bool State
)
```

### C++/CLI

```cpp
void IHighlight(
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`: True adds highlighting, false removes highlighting

## VBA Syntax

See [Face2::IHighlight](ms-its:sldworksapivb6.chm::/sldworks~Face2~IHighlight.html).

## Remarks

Highlighting remains in effect until the model is rebuilt or redrawn.

This method is not supported for faces obtained from reference surface bodies.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight.html)
[IEdge::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
