---
title: "InsertViewportByEntity Method (ISheet)"
project: ""
interface: "ISheet"
member: "InsertViewportByEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertViewportByEntity.html"
---

# InsertViewportByEntity Method (ISheet)

Converts the specified entity into a Viewport.

## Syntax

### Visual Basic

```vb
Function InsertViewportByEntity( _
   ByVal Entity As System.Object _
) As Viewport
```

### C#

```csharp
Viewport InsertViewportByEntity(
   System.object Entity
)
```

### JScript

```
function InsertViewportByEntity(
   Entity : System.Object
) : Viewport;
```

### Managed Extensions for C++

```
Viewport* InsertViewportByEntity(
   System.Object* Entity
)
```

### C++/CLI

```cpp
Viewport^ InsertViewportByEntity(
   System.Object^ Entity
)
```

### Parameters

- `Entity`: Entity to convert to a Viewport; valid entities are [2D PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html), [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html), [Ellipse](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html), [Region](Interop.dsAutomation~Interop.dsAutomation.IRegion.html), and closed [Spline](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)

### Return Value

[Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[ISheet::InsertPolygonalViewport Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertPolygonalViewport.html)
[ISheet::InsertRectangularViewport Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~InsertRectangularViewport.html)

## Availability

DraftSight V1R3.0
