---
title: "InsertPoint Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPoint.html"
---

# InsertPoint Method (ISketchManager)

Inserts a point.

## Syntax

### Visual Basic

```vb
Function InsertPoint( _
   ByVal PointX As System.Double, _
   ByVal PointY As System.Double, _
   ByVal PointZ As System.Double _
) As Point
```

### C#

```csharp
Point InsertPoint(
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

### JScript

```
function InsertPoint(
   PointX : System.double,
   PointY : System.double,
   PointZ : System.double
) : Point;
```

### Managed Extensions for C++

```
Point* InsertPoint(
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

### C++/CLI

```cpp
Point^ InsertPoint(
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

### Parameters

- `PointX`: x coordinate where to insert the point
- `PointY`: y coordinate where to insert the point
- `PointZ`: z coordinate where to insert the point

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IPoint.html)

## Examples

[Insert Point (C#)](Insert_Point_Example_CSharp.htm)
[Insert Point (VB.NET)](Insert_Point_Example_VBNET.htm)
[Insert Point (VBA)](Insert_Point_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.1
