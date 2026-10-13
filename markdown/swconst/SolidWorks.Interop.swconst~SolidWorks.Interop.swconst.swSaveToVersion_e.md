---
title: "swSaveToVersion_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSaveToVersion_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveToVersion_e.html"
---

# swSaveToVersion_e Enumeration

Previous version file formats available for save compatibility checks.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSaveToVersion_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSaveToVersion_e
```

### C#

```csharp
public enum swSaveToVersion_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSaveToVersion_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSaveToVersion_Antepenultimate | 2 = Save to the file format of the second most recent previous major release of SOLIDWORKS |
| swSaveToVersion_DoNotUpgrade | 0 = Save without upgrading it to a more recent file format |
| swSaveToVersion_Penultimate | 1 = Save to the file format of the most recent previous major release of SOLIDWORKS |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
