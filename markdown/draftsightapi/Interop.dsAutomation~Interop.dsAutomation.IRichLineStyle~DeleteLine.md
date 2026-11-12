---
title: "DeleteLine Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "DeleteLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~DeleteLine.html"
---

# DeleteLine Method (IRichLineStyle)

Deletes the specified line element from a RichLineStyle.

## Syntax

### Visual Basic

```vb
Sub DeleteLine( _
   ByVal VertexIndex As System.Integer _
)
```

### C#

```csharp
void DeleteLine(
   System.int VertexIndex
)
```

### JScript

```
function DeleteLine(
   VertexIndex : System.int
);
```

### Managed Extensions for C++

```
void DeleteLine(
   System.int VertexIndex
)
```

### C++/CLI

```cpp
void DeleteLine(
   System.int VertexIndex
)
```

### Parameters

- `VertexIndex`: Index of the line element to delete from the RichLineStyle (see **Remarks**)

## Remarks

Call [IRichLineStyle::GetLinesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLinesCount.html) to determine a valid value for VertexIndex.

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::AddLine Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~AddLine.html)

## Availability

DraftSight V1R1.3
