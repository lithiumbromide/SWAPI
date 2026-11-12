---
title: "GetClippedObject Method (IViewport)"
project: ""
interface: "IViewport"
member: "GetClippedObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~GetClippedObject.html"
---

# GetClippedObject Method (IViewport)

Gets the entity that defines the clipping boundary of the Viewport.

## Syntax

### Visual Basic

```vb
Function GetClippedObject( _
   ByRef ObjType As dsObjectType_e _
) As System.Object
```

### C#

```csharp
System.object GetClippedObject(
   out dsObjectType_e ObjType
)
```

### JScript

```
function GetClippedObject(
   ObjType : dsObjectType_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetClippedObject(
   [PARAMFLAG::Out] dsObjectType_e ObjType
)
```

### C++/CLI

```cpp
System.Object^ GetClippedObject(
   [Out] dsObjectType_e ObjType
)
```

### Parameters

- `ObjType`: Type of entity that defines the clipping boundary as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html) (see **Remarks**)

### Return Value

Entity that defines the clipping boundary: [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html), [Ellipse](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html), closed [PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html), [Region](Interop.dsAutomation~Interop.dsAutomation.IRegion.html), or closed [Spline](Interop.dsAutomation~Interop.dsAutomation.ISpline.html).

## Remarks

Before calling this method, call [IViewport::GetIsClipped](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetIsClipped.html) to determine if the Viewport is clipped.

Valid types of entities that can define the Viewport's clipping boundary are:

- dsObjectType_e.dsCircleType
- dsObjectType_e.dsEllipseArcType
- dsObjectType_e.dsPolyLineType
- dsObjectType_e.dsRegionType
- dsObjectType_e.dsSplineType

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)

## Availability

DraftSight V1R3.0
