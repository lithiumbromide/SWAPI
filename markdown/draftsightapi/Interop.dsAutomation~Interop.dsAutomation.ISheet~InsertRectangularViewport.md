---
title: "InsertRectangularViewport Method (ISheet)"
project: ""
interface: "ISheet"
member: "InsertRectangularViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertRectangularViewport.html"
---

# InsertRectangularViewport Method (ISheet)

Inserts a rectangular Viewport.

## Syntax

### Visual Basic

```vb
Function InsertRectangularViewport( _
   ByVal Mode As dsStandardViewports_e, _
   ByVal Fit As System.Boolean, _
   ByVal StartCorner As MathPoint, _
   ByVal OppositeCorner As MathPoint _
) As Viewport
```

### C#

```csharp
Viewport InsertRectangularViewport(
   dsStandardViewports_e Mode,
   System.bool Fit,
   MathPoint StartCorner,
   MathPoint OppositeCorner
)
```

### JScript

```
function InsertRectangularViewport(
   Mode : dsStandardViewports_e,
   Fit : System.boolean,
   StartCorner : MathPoint,
   OppositeCorner : MathPoint
) : Viewport;
```

### Managed Extensions for C++

```
Viewport* InsertRectangularViewport(
   dsStandardViewports_e Mode,
   System.bool Fit,
   MathPoint* StartCorner,
   MathPoint* OppositeCorner
)
```

### C++/CLI

```cpp
Viewport^ InsertRectangularViewport(
   dsStandardViewports_e Mode,
   System.bool Fit,
   MathPoint^ StartCorner,
   MathPoint^ OppositeCorner
)
```

### Parameters

- `Mode`: Type of Viewport as defined in [dsStandardViewports_e](Interop.dsAutomation~Interop.dsAutomation.dsStandardViewports_e.html)
- `Fit`: True to create a Viewport that fills the Sheet to the edges of the printable area, false to create a Viewport that fits the entire Sheet
- `StartCorner`: First corner [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the Viewport
- `OppositeCorner`: Second and opposite corner [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) from StartCorner for the Viewport

### Return Value

Rectangular [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## Examples

[Create Rectangular Viewport (C#)](Create_Rectangular_Viewport_Example_CSharp.htm)
[Create Rectangular Viewport (VB.NET)](Create_Rectangular_Viewport_Example_VBNET.htm)
[Create Rectangular Viewport (VBA)](Create_Rectangular_Viewport_Example_VBA.htm)
[Create Rectangular Viewport (JavaScript)](Create_Rectangular_Viewport_Example_JS.htm)

## See Also

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[ISheet::InsertPolygonalViewport Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertPolygonalViewport.html)
[ISheet::InsertViewportByEntity Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertViewportByEntity.html)

## Availability

DraftSight V1R3.0
