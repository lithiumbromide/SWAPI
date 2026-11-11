---
title: "GetCenter Method (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "GetCenter"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~GetCenter.html"
---

# GetCenter Method (IArcAlignedText)

Gets the center point of the curved text.

## Syntax

### Visual Basic

```vb
Sub GetCenter( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetCenter(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetCenter(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetCenter(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetCenter(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the center point
- `Y`: y coordinate of the center point
- `Z`: z coordinate of the center point

## See Also

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)
[IArcAlignedText::SetCenter Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~SetCenter.html)

## Availability

DraftSight 2018 SP2
