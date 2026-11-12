---
title: "SetPosition Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "SetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetPosition.html"
---

# SetPosition Method (ISimpleNote)

Sets the position for the SimpleNote.

## Syntax

### Visual Basic

```vb
Sub SetPosition( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetPosition(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetPosition(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetPosition(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetPosition(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate of the position
- `Y`: y coordinate of the position
- `Z`: z coordinate of the position

## Remarks

You can set the position, [alignment point](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetAlignmentPoint.html), or both, for the SimpleNote's text, depending on the [justification](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Justify.html).

## See Also

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::GetPosition Method](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetPosition.html)
[ISimpleNote::GetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetAlignmentPoint.html)
[ISimpleNote::Justify Property ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Justify.html)

## Availability

DraftSight V1R1.1
