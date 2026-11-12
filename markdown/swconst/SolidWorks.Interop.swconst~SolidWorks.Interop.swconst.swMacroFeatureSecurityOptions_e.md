---
title: "swMacroFeatureSecurityOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swMacroFeatureSecurityOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMacroFeatureSecurityOptions_e.html"
---

# swMacroFeatureSecurityOptions_e Enumeration

Macro feature security options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMacroFeatureSecurityOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMacroFeatureSecurityOptions_e
```

### C#

```csharp
public enum swMacroFeatureSecurityOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMacroFeatureSecurityOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMacroFeatureSecurityByDefault | 0 or 0x0 |
| swMacroFeatureSecurityCannotBeDeleted | 1 or 0x1 |
| swMacroFeatureSecurityCannotBeReplaced | 8 or 0x8 |
| swMacroFeatureSecurityCannotBeRolledBack | 32 or 0x20 |
| swMacroFeatureSecurityCannotBeSuppressed | 4 or 0x4 |
| swMacroFeatureSecurityEnableNote | 16 or 0x10 |
| swMacroFeatureSecurityNotEditable | 2 or 0x2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
