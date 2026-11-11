---
title: "SetLineStyle Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "SetLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~SetLineStyle.html"
---

# SetLineStyle Method (IRichLineStyle)

Sets the style name of the specified RichLineStyle.

## Syntax

### Visual Basic

```vb
Sub SetLineStyle( _
   ByVal VertexIndex As System.Integer, _
   ByVal StyleName As System.String _
)
```

### C#

```csharp
void SetLineStyle(
   System.int VertexIndex,
   System.string StyleName
)
```

### JScript

```
function SetLineStyle(
   VertexIndex : System.int,
   StyleName : System.String
);
```

### Managed Extensions for C++

```
void SetLineStyle(
   System.int VertexIndex,
   System.string* StyleName
)
```

### C++/CLI

```cpp
void SetLineStyle(
   System.int VertexIndex,
   System.String^ StyleName
)
```

### Parameters

- `VertexIndex`: Index of the line element whose style name to get (see **Remarks**)
- `StyleName`: Style name

## Remarks

Call [IRichLineStyle::GetLinesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLinesCount.html) to determine a valid value for VertexIndex.

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::GetLineStyle Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLineStyle.html)

## Availability

DraftSight V1R1.3
