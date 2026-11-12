---
title: "GetFitPointCoordinate Method (ISpline)"
project: ""
interface: "ISpline"
member: "GetFitPointCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~GetFitPointCoordinate.html"
---

# GetFitPointCoordinate Method (ISpline)

Gets the coordinates of the specified fit point of the Spline.

## Syntax

### Visual Basic

```vb
Function GetFitPointCoordinate( _
   ByVal Index As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool GetFitPointCoordinate(
   System.int Index,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetFitPointCoordinate(
   Index : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetFitPointCoordinate(
   System.int Index,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
System.bool GetFitPointCoordinate(
   System.int Index,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
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
[ISpline::SetFitPointCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~SetFitPointCoordinate.html)

## Availability

DraftSight V1R1.3
