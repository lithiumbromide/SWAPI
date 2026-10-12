---
title: "swSaveItemsPathError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSaveItemsPathError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveItemsPathError_e.html"
---

# swSaveItemsPathError_e Enumeration

Error return codes for [IAdvancedSaveAsOptions::ModifyItemsNameAndPath](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSaveItemsPathError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSaveItemsPathError_e
```

### C#

```csharp
public enum swSaveItemsPathError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSaveItemsPathError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSaveItemsPathError_ArraySizeNotMatching | 1 = Input arrays must be the same size |
| swSaveItemsPathError_InvalidPath | 2 = Path provided does not exist or user does not have write access |
| swSaveItemsPathError_Succeeded | 0 |
| swSaveItemsPathError_WrongComponentName | 3 = Name provided is not supported by SOLIDWORKS |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
