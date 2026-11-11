---
title: "AlignActiveCustomCoordinateSystemXYPlane Method (ICustomCoordinateSystemManager)"
project: ""
interface: "ICustomCoordinateSystemManager"
member: "AlignActiveCustomCoordinateSystemXYPlane"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemXYPlane.html"
---

# AlignActiveCustomCoordinateSystemXYPlane Method (ICustomCoordinateSystemManager)

Aligns the active coordinate system's xy plane in the specified direction with the specified origin.

## Syntax

### Visual Basic

```vb
Sub AlignActiveCustomCoordinateSystemXYPlane( _
   ByVal Origin As MathPoint, _
   ByVal XAxisThroughPoint As MathPoint, _
   ByVal XYPlaneThroughPoint As MathPoint _
)
```

### C#

```csharp
void AlignActiveCustomCoordinateSystemXYPlane(
   MathPoint Origin,
   MathPoint XAxisThroughPoint,
   MathPoint XYPlaneThroughPoint
)
```

### JScript

```
function AlignActiveCustomCoordinateSystemXYPlane(
   Origin : MathPoint,
   XAxisThroughPoint : MathPoint,
   XYPlaneThroughPoint : MathPoint
);
```

### Managed Extensions for C++

```
void AlignActiveCustomCoordinateSystemXYPlane(
   MathPoint* Origin,
   MathPoint* XAxisThroughPoint,
   MathPoint* XYPlaneThroughPoint
)
```

### C++/CLI

```cpp
void AlignActiveCustomCoordinateSystemXYPlane(
   MathPoint^ Origin,
   MathPoint^ XAxisThroughPoint,
   MathPoint^ XYPlaneThroughPoint
)
```

### Parameters

- `Origin`: Custom coordinate system's [origin](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `XAxisThroughPoint`: Direction [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the x axis of the coordinate system (see **Remarks**)
- `XYPlaneThroughPoint`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) to describe the xy plane of the coordinate system (see **Remarks**)

## Remarks

The point specified for XYPlaneThroughPoint specifies which plane the y axis is in and the direction of the y axis orthogonal to XAxisThroughPoint, resulting in a vector that is orthogonal to the x and y axes.

There are two possible orthogonal vectors for the z axis, depending on the direction of the y axis. Both vectors have the same XAxisThroughPoint; however, both the y and z axis are in different directions, depending on XYPlaneThroughPoint.

## See Also

[ICustomCoordinateSystemManager Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager.html)
[ICustomCoordinateSystemManager Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager_members.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemByEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemByEntity.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemByView Method ()](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemByView.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemZAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemZAxis.html)

## Availability

DraftSight V1R5.0
