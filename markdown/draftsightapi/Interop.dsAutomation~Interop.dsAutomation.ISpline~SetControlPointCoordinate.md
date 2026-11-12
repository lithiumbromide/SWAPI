---
title: "SetControlPointCoordinate Method (ISpline)"
project: ""
interface: "ISpline"
member: "SetControlPointCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~SetControlPointCoordinate.html"
---

# SetControlPointCoordinate Method (ISpline)

Sets the coordinates of a control point of the Spline.

## Syntax

### Visual Basic

```vb
Function SetControlPointCoordinate( _
   ByVal Index As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool SetControlPointCoordinate(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetControlPointCoordinate(
   Index : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetControlPointCoordinate(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetControlPointCoordinate(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `Index`: Index of the control point (see **Remarks**)
- `X`: x coordinate of the control point
- `Y`: y coordinate of the control point
- `Z`: z coordinate of the control point

### Return Value

True if successful, false if not

## Remarks

Before calling this method, call [ISpline::GetControlPointsCount](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetControlPointsCount.html) to determine a valid value for Index.

## See Also

[ISpline Interface](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
[ISpline Members](Interop.dsAutomation~Interop.dsAutomation.ISpline_members.html)
[ISpline::GetControlPointCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetControlPointCoordinate.html)

## Availability

DraftSight V1R1.3
