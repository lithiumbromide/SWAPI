---
title: "Display Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "Display"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Display.html"
---

# Display Method (IEdge)

Highlights this edge with the specified color.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Display( _
   ByVal Width As System.Integer, _
   ByVal Red As System.Double, _
   ByVal Green As System.Double, _
   ByVal Blue As System.Double, _
   ByVal HighlightState As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Width As System.Integer
Dim Red As System.Double
Dim Green As System.Double
Dim Blue As System.Double
Dim HighlightState As System.Boolean

instance.Display(Width, Red, Green, Blue, HighlightState)
```

### C#

```csharp
void Display(
   System.int Width,
   System.double Red,
   System.double Green,
   System.double Blue,
   System.bool HighlightState
)
```

### C++/CLI

```cpp
void Display(
   System.int Width,
   System.double Red,
   System.double Green,
   System.double Blue,
   System.bool HighlightState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Highlight width
- `Red`: Red value of RGB value for the color, between 0 and 1
- `Green`: Green value of RGB value for the color, between 0 and 1
- `Blue`: Blue value if RGB value for the color, between 0 and 1
- `HighlightState`: True if the edge is highlighted, false if not

## VBA Syntax

See [Edge::Display](ms-its:sldworksapivb6.chm::/sldworks~Edge~Display.html).

## Examples

[Add Highlighting to or Remove Highlighting From Edges (VBA)](Add_Highlighting_to_or_Remove_Highlight_from_Edges_Example_VB.htm)
[Get Faces Affected by Feature (VBA)](Get_Faces_Affected_by_Feature_Example_VB.htm)

## Remarks

To show the same edge with a different color, hide it and then set a different color. SOLIDWORKS shows the edge in the specified color until you hide it. Rotation, zoom, other repaint actions do not cause the edge to disappear.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IFace2::IHighlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight.html)
[IFace2::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight.html)
[IVertex::Display Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~Display.html)
[IEdge::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
