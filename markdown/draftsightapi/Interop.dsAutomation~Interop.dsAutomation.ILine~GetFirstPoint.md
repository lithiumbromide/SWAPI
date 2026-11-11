---
title: "GetFirstPoint Method (ILine)"
project: ""
interface: "ILine"
member: "GetFirstPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~GetFirstPoint.html"
---

# GetFirstPoint Method (ILine)

Gets the point that starts the Line.

## Syntax

### Visual Basic

```vb
Sub GetFirstPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetFirstPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetFirstPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetFirstPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetFirstPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the point that starts the Line
- `Y`: y coordinate of the point that starts the Line
- `Z`: z coordinate of the point that starts the Line

## See Also

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[ILine::GetSecondPoint Method](Interop.dsAutomation~Interop.dsAutomation.ILine~GetSecondPoint.html)
[ILine::SetFirstPoint Method](Interop.dsAutomation~Interop.dsAutomation.ILine~SetFirstPoint.html)
[ILine::SetSecondPoint Method](Interop.dsAutomation~Interop.dsAutomation.ILine~SetSecondPoint.html)

## Availability

DraftSight V1R1.1
