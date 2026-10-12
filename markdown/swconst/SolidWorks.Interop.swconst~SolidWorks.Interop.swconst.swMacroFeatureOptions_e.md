---
title: "swMacroFeatureOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swMacroFeatureOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMacroFeatureOptions_e.html"
---

# swMacroFeatureOptions_e Enumeration

Placement of the macro feature in the FeatureManager design tree options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMacroFeatureOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMacroFeatureOptions_e
```

### C#

```csharp
public enum swMacroFeatureOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMacroFeatureOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMacroFeatureAlwaysAtEnd | 1 or 0x1 |
| swMacroFeatureByDefault | 0 or 0x0 |
| swMacroFeatureEmbedMacroFile | 16 or 0x10; not supported by programming languages for the Microsoft .NET Framework; for example, not supported by C#, Visual Basic .NET, or Managed C++ |
| swMacroFeatureIsDragable | 4 or 0x4 |
| swMacroFeatureIsPatternable | 2 or 0x2 |
| swMacroFeatureNoCachedBody | 8 or 0x8; do not serialize cached body in macro feature |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
