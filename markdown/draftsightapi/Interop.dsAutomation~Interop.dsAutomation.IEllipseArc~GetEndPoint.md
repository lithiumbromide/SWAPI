---
title: "GetEndPoint Method (IEllipseArc)"
project: ""
interface: "IEllipseArc"
member: "GetEndPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetEndPoint.html"
---

# GetEndPoint Method (IEllipseArc)

Gets the axis end point of an Ellipse or an elliptical Arc.

## Syntax

### Visual Basic

```vb
Sub GetEndPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetEndPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetEndPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetEndPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetEndPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the axis end point
- `Y`: y coordinate of the axis end point
- `Z`: z coordinate of the axis end point

## See Also

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[IEllipseArc::GetCenter Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetCenter.html)
[IEllipseArc::GetStartPoint Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetStartPoint.html)

## Availability

DraftSight V1R1.1
