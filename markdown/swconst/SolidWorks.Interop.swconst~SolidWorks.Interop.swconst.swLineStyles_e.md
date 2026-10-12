---
title: "swLineStyles_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swLineStyles_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLineStyles_e.html"
---

# swLineStyles_e Enumeration

Line styles used in drawings.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swLineStyles_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swLineStyles_e
```

### C#

```csharp
public enum swLineStyles_e : System.Enum
```

### C++/CLI

```cpp
public enum class swLineStyles_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swLineCENTER | 4 |
| swLineCHAIN | 3 |
| swLineCHAINTHICK | 6 = Thin/Thick Chain |
| swLineCONTINUOUS | 0 = Solid |
| swLineDEFAULT | 7 |
| swLineHIDDEN | 1 = Dashed |
| swLinePHANTOM | 2 |
| swLineSTITCH | 5 |

## Remarks

Open a drawing and view line style appearances in **Tools > Options > Document Properties > Line Style**.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
