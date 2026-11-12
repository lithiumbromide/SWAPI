---
title: "GetVertex2Coordinate Method (ISolid)"
project: ""
interface: "ISolid"
member: "GetVertex2Coordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex2Coordinate.html"
---

# GetVertex2Coordinate Method (ISolid)

Gets the coordinates of the second vertex of the 2D Solid.

## Syntax

### Visual Basic

```vb
Sub GetVertex2Coordinate( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetVertex2Coordinate(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetVertex2Coordinate(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetVertex2Coordinate(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetVertex2Coordinate(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the second vertex
- `Y`: y coordinate of the second vertex
- `Z`: z coordinate of the second vertex

## See Also

[ISolid Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)
[ISolid Members](Interop.dsAutomation~Interop.dsAutomation.ISolid_members.html)
[ISolid::GetVertex1Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex1Coordinate.html)
[ISolid::GetVertex3Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex3Coordinate.html)
[ISolid::GetVertex4Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex4Coordinate.html)
[ISolid::SetVertex1Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex1Coordinate.html)
[ISolid::SetVertex2Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex2Coordinate.html)
[ISolid::SetVertex3Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex3Coordinate.html)
[ISolid::SetVertex4Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex4Coordinate.html)

## Availability

DraftSight V1R1.3
