---
title: "GetSecondPoint Method (ILine)"
project: ""
interface: "ILine"
member: "GetSecondPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~GetSecondPoint.html"
---

# GetSecondPoint Method (ILine)

Gets the point that ends the Line.

## Syntax

### Visual Basic

```vb
Sub GetSecondPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetSecondPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetSecondPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetSecondPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetSecondPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the point that ends the Line
- `Y`: y coordinate of the point that ends the Line
- `Z`: z coordinate of the point that ends the Line

## See Also

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[ILine::SetFirstPoint Method](Interop.dsAutomation~Interop.dsAutomation.ILine~SetFirstPoint.html)
[ILine::SetSecondPoint Method](Interop.dsAutomation~Interop.dsAutomation.ILine~SetSecondPoint.html)
[ILine::GetFirstPoint Method](Interop.dsAutomation~Interop.dsAutomation.ILine~GetFirstPoint.html)

## Availability

DraftSight V1R1.1
