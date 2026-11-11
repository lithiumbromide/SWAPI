---
title: "AddLine Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "AddLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~AddLine.html"
---

# AddLine Method (IRichLineStyle)

Adds a line element to a RichLineStyle.

## Syntax

### Visual Basic

```vb
Sub AddLine( _
   ByVal Offset As System.Double, _
   ByVal LineColor As Color, _
   ByVal StyleName As System.String _
)
```

### C#

```csharp
void AddLine(
   System.double Offset,
   Color LineColor,
   System.string StyleName
)
```

### JScript

```
function AddLine(
   Offset : System.double,
   LineColor : Color,
   StyleName : System.String
);
```

### Managed Extensions for C++

```
void AddLine(
   System.double Offset,
   Color* LineColor,
   System.string* StyleName
)
```

### C++/CLI

```cpp
void AddLine(
   System.double Offset,
   Color^ LineColor,
   System.String^ StyleName
)
```

### Parameters

- `Offset`: Offset
- `LineColor`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)
- `StyleName`: Name of the RichLineStyle where to add the line element

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::DeleteLine Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~DeleteLine.html)

## Availability

DraftSight V1R1.3
