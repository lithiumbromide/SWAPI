---
title: "GetPosition Method (IShape)"
project: ""
interface: "IShape"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IShape~GetPosition.html"
---

# GetPosition Method (IShape)

Gets the insertion point of the shape.

## Syntax

### Visual Basic

```vb
Sub GetPosition( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetPosition(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetPosition(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetPosition(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetPosition(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the insertion point
- `Y`: y coordinate of the insertion point
- `Z`: z coordinate of the insertion point

## See Also

[IShape Interface](Interop.dsAutomation~Interop.dsAutomation.IShape.html)
[IShape Members](Interop.dsAutomation~Interop.dsAutomation.IShape_members.html)
[IShape::SetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.IShape~SetPosition.html)

## Availability

DraftSight V1R4.0
