---
title: "GetVertex2Coordinate Method (IFace)"
project: ""
interface: "IFace"
member: "GetVertex2Coordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IFace~GetVertex2Coordinate.html"
---

# GetVertex2Coordinate Method (IFace)

Gets the coordinates of the second vertex of the Face.

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

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## See Also

[IFace Interface](Interop.dsAutomation~Interop.dsAutomation.IFace.html)
[IFace Members](Interop.dsAutomation~Interop.dsAutomation.IFace_members.html)
[IFace::SetVertex2Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.IFace~SetVertex2Coordinate.html)
[IFace::GetVertex1Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.IFace~GetVertex1Coordinate.html)
[IFace::GetVertex3Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.IFace~GetVertex3Coordinate.html)
[IFace::GetVertex4Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.IFace~GetVertex4Coordinate.html)
[IFace::SetVertex1Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.IFace~SetVertex1Coordinate.html)
[IFace::SetVertex3Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.IFace~SetVertex3Coordinate.html)
[IFace::SetVertex4Coordinate Method](Interop.dsAutomation~Interop.dsAutomation.IFace~SetVertex4Coordinate.html)

## Availability

DraftSight V1R1.3
