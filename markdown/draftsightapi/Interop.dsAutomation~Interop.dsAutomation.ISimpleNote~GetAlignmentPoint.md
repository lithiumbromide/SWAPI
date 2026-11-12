---
title: "GetAlignmentPoint Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "GetAlignmentPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetAlignmentPoint.html"
---

# GetAlignmentPoint Method (ISimpleNote)

Gets the alignment point of the SimpleNote.

## Syntax

### Visual Basic

```vb
Sub GetAlignmentPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetAlignmentPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetAlignmentPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetAlignmentPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetAlignmentPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the alignment point
- `Y`: y coordinate of the alignment point
- `Z`: z coordinate of the alignment point

## See Also

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::SetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetAlignmentPoint.html)
[ISimpleNote::GetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetPosition.html)
[ISimpleNote::SetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetPosition.html)
[ISimpleNote::Justify Property ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Justify.html)

## Availability

DraftSight V1R5.0
