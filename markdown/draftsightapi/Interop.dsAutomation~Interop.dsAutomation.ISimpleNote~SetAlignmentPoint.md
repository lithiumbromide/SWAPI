---
title: "SetAlignmentPoint Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "SetAlignmentPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetAlignmentPoint.html"
---

# SetAlignmentPoint Method (ISimpleNote)

Sets the alignment point for the SimpleNote.

## Syntax

### Visual Basic

```vb
Sub SetAlignmentPoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetAlignmentPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetAlignmentPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetAlignmentPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetAlignmentPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate of the alignment point
- `Y`: y coordinate of the alignment point
- `Z`: z coordinate of the alignment point

## Remarks

You can set the alignment point, [position](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetPosition.html), or both, for the SimpleNote's text, depending on the [justification](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Justify.html).

## See Also

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::GetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetAlignmentPoint.html)
[ISimpleNote::GetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetPosition.html)

## Availability

DraftSight V1R5.0
