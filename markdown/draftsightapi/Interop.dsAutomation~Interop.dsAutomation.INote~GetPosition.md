---
title: "GetPosition Method (INote)"
project: ""
interface: "INote"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote~GetPosition.html"
---

# GetPosition Method (INote)

Gets the upper-left corner coordinates of the Note.

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

- `X`: x coordinate of the upper-left corner of the Note
- `Y`: y coordinate of the upper-left corner of the Note
- `Z`: z coordinate of the upper-left corner of the Note

## See Also

[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[INote::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.INote~SetPosition.html)

## Availability

DraftSight V1R1.1
