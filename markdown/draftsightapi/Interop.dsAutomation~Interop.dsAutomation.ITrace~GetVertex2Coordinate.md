---
title: "GetVertex2Coordinate Method (ITrace)"
project: ""
interface: "ITrace"
member: "GetVertex2Coordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITrace~GetVertex2Coordinate.html"
---

# GetVertex2Coordinate Method (ITrace)

Gets the x, y, and z coordinates of the second vertex of this Trace.

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

## Examples

See the [ITrace](Interop.dsAutomation~Interop.dsAutomation.ITrace.html) examples.

## See Also

[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
[ITrace Members](Interop.dsAutomation~Interop.dsAutomation.ITrace_members.html)
[ITrace::SetVertex2Coordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~SetVertex2Coordinate.html)
[ITrace::GetVertex1Coordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~GetVertex1Coordinate.html)
[ITrace::SetVertex1Coordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~SetVertex1Coordinate.html)
[ITrace::GetVertex3Coordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~GetVertex3Coordinate.html)
[ITrace::SetVertex3Coordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~SetVertex3Coordinate.html)
[ITrace::GetVertex4Coordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~GetVertex4Coordinate.html)
[ITrace::SetVertex4Coordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~SetVertex4Coordinate.html)

## Availability

DraftSight V1R5.0
