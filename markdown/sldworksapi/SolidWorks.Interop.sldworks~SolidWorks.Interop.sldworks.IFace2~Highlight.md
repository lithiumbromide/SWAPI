---
title: "Highlight Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "Highlight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight.html"
---

# Highlight Method (IFace2)

Adds highlighting to or removes highlighting from a face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Highlight( _
   ByVal State As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
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

- `State`: True adds highlighting, false removes highlighting

## VBA Syntax

See [Face2::Highlight](ms-its:sldworksapivb6.chm::/sldworks~Face2~Highlight.html).

## Examples

[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)

## Remarks

Highlighting remains in effect until the model is rebuilt or redrawn.

This method is not supported for faces obtained from reference surface bodies.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IHighlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight.html)
[IEdge::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
