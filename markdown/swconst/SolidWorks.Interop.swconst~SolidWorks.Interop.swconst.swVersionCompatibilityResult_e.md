---
title: "swVersionCompatibilityResult_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swVersionCompatibilityResult_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swVersionCompatibilityResult_e.html"
---

# swVersionCompatibilityResult_e Enumeration

Results for file version compatibility checks.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swVersionCompatibilityResult_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swVersionCompatibilityResult_e
```

### C#

```csharp
public enum swVersionCompatibilityResult_e : System.Enum
```

### C++/CLI

```cpp
public enum class swVersionCompatibilityResult_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swVersionCompatibilityResult_Completed | 0 = Success. No incompatibility found. |
| swVersionCompatibilityResult_FailFileNotResolved | 2 = Failure. The file could not be resolved. |
| swVersionCompatibilityResult_FailInvalidVersion | 3 = Failure. The requested version is not valid for compatibility checks. (See swSaveToVersion_e ) |
| swVersionCompatibilityResult_FailUnknown | 1 = Failure. The file contains features incompatible with the specified version, or could not be checked. |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
