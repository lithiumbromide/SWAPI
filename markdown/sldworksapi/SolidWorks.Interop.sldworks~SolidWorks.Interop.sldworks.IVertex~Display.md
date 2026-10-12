---
title: "Display Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "Display"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~Display.html"
---

# Display Method (IVertex)

Highlights the vertex in the specified color.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Display( _
   ByVal TopDoc As ModelDoc2, _
   ByVal Color As System.Integer, _
   ByVal Scale As System.Double, _
   ByVal HighlightState As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim TopDoc As ModelDoc2
Dim Color As System.Integer
Dim Scale As System.Double
Dim HighlightState As System.Boolean

instance.Display(TopDoc, Color, Scale, HighlightState)
```

### C#

```csharp
void Display(
   ModelDoc2 TopDoc,
   System.int Color,
   System.double Scale,
   System.bool HighlightState
)
```

### C++/CLI

```cpp
void Display(
   ModelDoc2^ TopDoc,
   System.int Color,
   System.double Scale,
   System.bool HighlightState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`: [Model](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) in which to display the vertex
- `Color`: COLORREF value for highlighting
- `Scale`: Radius of the circle used to display the vertex

  NOTE: Vertex is displayed as a circle. By default, the radius is 4 pixels. Therefore, a scale of 1 is equal to 4 pixels.
- `HighlightState`: True to highlight the vertex, false to not

## VBA Syntax

See [Vertex::Display](ms-its:sldworksapivb6.chm::/sldworks~Vertex~Display.html).

## Examples

[Display Vertices (VBA)](Display_Vertices_Example_VB.htm)

## Remarks

| If HighlightState set to... | Then the vertex is... |
| --- | --- |
| True | Highlighted in the color specified for Color |
| False | Hidden and Color is ignored |

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
