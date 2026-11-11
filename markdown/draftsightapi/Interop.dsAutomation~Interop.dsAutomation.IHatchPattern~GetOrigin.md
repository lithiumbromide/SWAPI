---
title: "GetOrigin Method (IHatchPattern)"
project: ""
interface: "IHatchPattern"
member: "GetOrigin"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetOrigin.html"
---

# GetOrigin Method (IHatchPattern)

Gets the origin of the Hatch pattern line.

## Syntax

### Visual Basic

```vb
Sub GetOrigin( _
   ByRef X As System.Double, _
   ByRef Y As System.Double _
)
```

### C#

```csharp
void GetOrigin(
   out System.double X,
   out System.double Y
)
```

### JScript

```
function GetOrigin(
   X : System.double,
   Y : System.double
);
```

### Managed Extensions for C++

```
void GetOrigin(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y
)
```

### C++/CLI

```cpp
void GetOrigin(
   [Out] System.double X,
   [Out] System.double Y
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate

## See Also

[IHatchPattern Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern.html)
[IHatchPattern Members](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern_members.html)
[IHatchPattern::SetOrigin Method](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetOrigin.html)

## Availability

DraftSight V1R1.3
