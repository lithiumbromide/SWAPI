---
title: "GetIsClipped Method (IViewport)"
project: ""
interface: "IViewport"
member: "GetIsClipped"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~GetIsClipped.html"
---

# GetIsClipped Method (IViewport)

Gets whether the Viewport is clipped by an entity.

## Syntax

### Visual Basic

```vb
Sub GetIsClipped( _
   ByRef IsClipped As System.Boolean _
)
```

### C#

```csharp
void GetIsClipped(
   out System.bool IsClipped
)
```

### JScript

```
function GetIsClipped(
   IsClipped : System.boolean
);
```

### Managed Extensions for C++

```
void GetIsClipped(
   [PARAMFLAG::Out] System.bool IsClipped
)
```

### C++/CLI

```cpp
void GetIsClipped(
   [Out] System.bool IsClipped
)
```

### Parameters

- `IsClipped`: True if the Viewport is clipped by an entity, false if the Viewport is not clipped by an entity (see **Remarks**)

## Examples

[Create Rectangular Viewport (C#)](Create_Rectangular_Viewport_Example_CSharp.htm)
[Create Rectangular Viewport (VB.NET)](Create_Rectangular_Viewport_Example_VBNET.htm)
[Create Rectangular Viewport (VBA)](Create_Rectangular_Viewport_Example_VBA.htm)

## Remarks

These entities can define the clipping boundary of a Viewport: [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html), [Ellipse](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html), closed [PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html), [Region](Interop.dsAutomation~Interop.dsAutomation.IRegion.html), or closed [Spline](Interop.dsAutomation~Interop.dsAutomation.ISpline.html). After calling this method, call [IViewport::GetClippedObject](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetClippedObject.html) to get the entity that defines the clipping boundary.

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)

## Availability

DraftSight V1R3.0
