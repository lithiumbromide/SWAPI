---
title: "GetControlPointCoordinate Method (ISpline)"
project: ""
interface: "ISpline"
member: "GetControlPointCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~GetControlPointCoordinate.html"
---

# GetControlPointCoordinate Method (ISpline)

Gets the coordinates of the specified control point of the Spline.

## Syntax

### Visual Basic

```vb
Function GetControlPointCoordinate( _
   ByVal Index As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool GetControlPointCoordinate(
   System.int Index,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetControlPointCoordinate(
   Index : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetControlPointCoordinate(
   System.int Index,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
System.bool GetControlPointCoordinate(
   System.int Index,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
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
[ISpline::SetControlPointCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~SetControlPointCoordinate.html)

## Availability

DraftSight V1R1.3
