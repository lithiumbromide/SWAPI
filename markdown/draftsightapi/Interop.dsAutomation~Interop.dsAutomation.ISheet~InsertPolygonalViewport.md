---
title: "InsertPolygonalViewport Method (ISheet)"
project: ""
interface: "ISheet"
member: "InsertPolygonalViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertPolygonalViewport.html"
---

# InsertPolygonalViewport Method (ISheet)

Inserts a polygonal Viewport in the sheet.

## Syntax

### Visual Basic

```vb
Function InsertPolygonalViewport( _
   ByVal VerticesCoordinateDblArray As System.Object _
) As Viewport
```

### C#

```csharp
Viewport InsertPolygonalViewport(
   System.object VerticesCoordinateDblArray
)
```

### JScript

```
function InsertPolygonalViewport(
   VerticesCoordinateDblArray : System.Object
) : Viewport;
```

### Managed Extensions for C++

```
Viewport* InsertPolygonalViewport(
   System.Object* VerticesCoordinateDblArray
)
```

### C++/CLI

```cpp
Viewport^ InsertPolygonalViewport(
   System.Object^ VerticesCoordinateDblArray
)
```

### Parameters

- `VerticesCoordinateDblArray`: Array of doubles of the x, y, and z coordinates indicating the point that defines the boundary for the polygonal Viewport

### Return Value

Polygonal [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[ISheet::InsertRectangularViewport Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertRectangularViewport.html)
[ISheet::InsertViewportByEntity Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertViewportByEntity.html)

## Availability

DraftSight V1R3.0
