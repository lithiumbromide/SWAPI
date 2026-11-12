---
title: "swCloseReopenOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCloseReopenOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCloseReopenOption_e.html"
---

# swCloseReopenOption_e Enumeration

File close and reopen options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCloseReopenOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCloseReopenOption_e
```

### C#

```csharp
public enum swCloseReopenOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCloseReopenOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCloseReopenOption_DiscardChanges | 2 or 0x2; include this option to discard any changes to the document before reopening it; if you exclude this option and there are changes, ISldWorks::CloseAndReopen fails and returns swCloseReopenError_e.swCloseReopenModifiedError |
| swCloseReopenOption_ExitDetailingMode | 8 or 0x8; include this option to reopen model drawings as resolved; if excluded by ISldWorks::CloseAndReopen2, keeps a model drawing in detailing mode on reopen |
| swCloseReopenOption_MatchSheet | 4 or 0x4; include this option to open the same sheet that was active during closing |
| swCloseReopenOption_ReadOnly | 1 or 0x1; include this option to open the drawing document in read-only mode |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
