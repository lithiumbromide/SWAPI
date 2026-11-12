---
title: "swPropMgrPageOptionStyle_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropMgrPageOptionStyle_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageOptionStyle_e.html"
---

# swPropMgrPageOptionStyle_e Enumeration

PropertyManage page group option styles. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropMgrPageOptionStyle_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropMgrPageOptionStyle_e
```

### C#

```csharp
public enum swPropMgrPageOptionStyle_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropMgrPageOptionStyle_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropMgrPageOptionStyle_FirstInGroup | 1 or 0x1; This is the beginning of a group of option items; any following option items without this value set are considered part of the group; the next option with this value set indicates the start of a new option group |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
