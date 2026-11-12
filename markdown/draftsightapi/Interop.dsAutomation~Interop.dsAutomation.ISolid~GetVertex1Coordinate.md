---
title: "GetVertex1Coordinate Method (ISolid)"
project: ""
interface: "ISolid"
member: "GetVertex1Coordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex1Coordinate.html"
---

# GetVertex1Coordinate Method (ISolid)

Gets the coordinates of the first vertex of the 2D Solid.

## Syntax

### Visual Basic

```vb
Sub GetVertex1Coordinate( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetVertex1Coordinate(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetVertex1Coordinate(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetVertex1Coordinate(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetVertex1Coordinate(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the first vertex
- `Y`: y coordinate of the first vertex
- `Z`: z coordinate of the first vertex

## See Also

[ISolid Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)
[ISolid Members](Interop.dsAutomation~Interop.dsAutomation.ISolid_members.html)
[ISolid::GetVertex2Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex2Coordinate.html)
[ISolid::GetVertex3Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex3Coordinate.html)
[ISolid::GetVertex4Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex4Coordinate.html)
[ISolid::SetVertex1Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex1Coordinate.html)
[ISolid::SetVertex2Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex2Coordinate.html)
[ISolid::SetVertex3Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex3Coordinate.html)
[ISolid::SetVertex4Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex4Coordinate.html)

## Availability

DraftSight V1R1.3
