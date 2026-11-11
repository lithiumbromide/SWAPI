---
title: "GetPosition Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetPosition.html"
---

# GetPosition Method (ISimpleNote)

Gets the position of the SimpleNote.

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

- `X`: x coordinate of the position
- `Y`: y coordinate of the position
- `Z`: z coordinate of the position

## See Also

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetPosition.html)
[ISimpleNote::GetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetAlignmentPoint.html)
[ISimpleNote::SetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetAlignmentPoint.html)
[ISimpleNote::Justify Property ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Justify.html)

## Availability

DraftSight V1R1.1
