---
title: "SetFitPointCoordinate Method (ISpline)"
project: ""
interface: "ISpline"
member: "SetFitPointCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~SetFitPointCoordinate.html"
---

# SetFitPointCoordinate Method (ISpline)

Sets the coordinates of a fit point of the Spline.

## Syntax

### Visual Basic

```vb
Function SetFitPointCoordinate( _
   ByVal Index As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool SetFitPointCoordinate(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetFitPointCoordinate(
   Index : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetFitPointCoordinate(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetFitPointCoordinate(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `Index`: Index of the fit point (see **Remarks**)
- `X`: x coordinate of the fit point
- `Y`: y coordinate of the fit point
- `Z`: z coordinate of the fit point

### Return Value

True if successful, false if not

## Remarks

Before calling this method, call [ISpline::GetFitPointsCount](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetFitPointsCount.html) to determine a valid value for Index.

## See Also

[ISpline Interface](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
[ISpline Members](Interop.dsAutomation~Interop.dsAutomation.ISpline_members.html)
[ISpline::GetFitPointCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetFitPointCoordinate.html)

## Availability

DraftSight V1R1.3
