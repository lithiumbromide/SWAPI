---
title: "SetLineOffset Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "SetLineOffset"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~SetLineOffset.html"
---

# SetLineOffset Method (IRichLineStyle)

Sets the offset of the specified RichLineStyle.

## Syntax

### Visual Basic

```vb
Sub SetLineOffset( _
   ByVal VertexIndex As System.Integer, _
   ByVal Offset As System.Double _
)
```

### C#

```csharp
void SetLineOffset(
   System.int VertexIndex,
   System.double Offset
)
```

### JScript

```
function SetLineOffset(
   VertexIndex : System.int,
   Offset : System.double
);
```

### Managed Extensions for C++

```
void SetLineOffset(
   System.int VertexIndex,
   System.double Offset
)
```

### C++/CLI

```cpp
void SetLineOffset(
   System.int VertexIndex,
   System.double Offset
)
```

### Parameters

- `VertexIndex`: Index of the line element whose offset to set
- `Offset`: Offset value

## Remarks

Call [IRichLineStyle::GetLinesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLinesCount.html) to determine a valid value for VertexIndex.

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::GetLineOffset Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLineOffset.html)

## Availability

DraftSight V1R1.3
