---
title: "GetVertex3Coordinate Method (ISolid)"
project: ""
interface: "ISolid"
member: "GetVertex3Coordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex3Coordinate.html"
---

# GetVertex3Coordinate Method (ISolid)

Gets the coordinates of the third vertex of the 2D Solid.

## Syntax

### Visual Basic

```vb
Sub GetVertex3Coordinate( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetVertex3Coordinate(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetVertex3Coordinate(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetVertex3Coordinate(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetVertex3Coordinate(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the third vertex
- `Y`: y coordinate of the third vertex
- `Z`: z coordinate of the third vertex

## See Also

[ISolid Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)
[ISolid Members](Interop.dsAutomation~Interop.dsAutomation.ISolid_members.html)
[ISolid::GetVertex1Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex1Coordinate.html)
[ISolid::GetVertex2Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex2Coordinate.html)
[ISolid::GetVertex4Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetVertex4Coordinate.html)
[ISolid::SetVertex1Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex1Coordinate.html)
[ISolid::SetVertex2Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex2Coordinate.html)
[ISolid::SetVertex3Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex3Coordinate.html)
[ISolid::SetVertex4Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetVertex4Coordinate.html)

## Availability

DraftSight V1R1.3
