---
title: "GetLineOffset Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "GetLineOffset"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLineOffset.html"
---

# GetLineOffset Method (IRichLineStyle)

Gets the offset of the specified RichLineStyle.

## Syntax

### Visual Basic

```vb
Function GetLineOffset( _
   ByVal VertexIndex As System.Integer _
) As System.Double
```

### C#

```csharp
System.double GetLineOffset(
   System.int VertexIndex
)
```

### JScript

```
function GetLineOffset(
   VertexIndex : System.int
) : System.double;
```

### Managed Extensions for C++

```
System.double GetLineOffset(
   System.int VertexIndex
)
```

### C++/CLI

```cpp
System.double GetLineOffset(
   System.int VertexIndex
)
```

### Parameters

- `VertexIndex`: Index of the line element whose offset to get (see **Remarks**)

### Return Value

Offset value

## Remarks

Call [IRichLineStyle::GetLinesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLinesCount.html) to determine a valid value for VertexIndex.

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::SetLineOffset Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~SetLineOffset.html)

## Availability

DraftSight V1R1.3
