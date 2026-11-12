---
title: "swPropMgrPageTextBoxStyle_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropMgrPageTextBoxStyle_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageTextBoxStyle_e.html"
---

# swPropMgrPageTextBoxStyle_e Enumeration

PropertyManager page textbox styles. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropMgrPageTextBoxStyle_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropMgrPageTextBoxStyle_e
```

### C#

```csharp
public enum swPropMgrPageTextBoxStyle_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropMgrPageTextBoxStyle_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropMgrPageTextBoxStyle_Multiline | 8 or 0x8 |
| swPropMgrPageTextBoxStyle_NoBorder | 4 or 0x4 |
| swPropMgrPageTextBoxStyle_NotifyOnlyWhenFocusLost | 1 or 0x1; Do not send notification every time a character in the text box changes; instead, only send notification when text box loses focus after the user has made all changes |
| swPropMgrPageTextBoxStyle_ReadOnly | 2 or 0x2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
