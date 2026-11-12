---
title: "GetLineStyle Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "GetLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLineStyle.html"
---

# GetLineStyle Method (IRichLineStyle)

Gets the style name of the specified RichLineStyle.

## Syntax

### Visual Basic

```vb
Function GetLineStyle( _
   ByVal VertexIndex As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetLineStyle(
   System.int VertexIndex
)
```

### JScript

```
function GetLineStyle(
   VertexIndex : System.int
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetLineStyle(
   System.int VertexIndex
)
```

### C++/CLI

```cpp
System.String^ GetLineStyle(
   System.int VertexIndex
)
```

### Parameters

- `VertexIndex`: Index of the line element whose style name to get

### Return Value

Style name

## Remarks

Call [IRichLineStyle::GetLinesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLinesCount.html) to determine a valid value for VertexIndex.

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)

## Availability

DraftSight V1R1.3
