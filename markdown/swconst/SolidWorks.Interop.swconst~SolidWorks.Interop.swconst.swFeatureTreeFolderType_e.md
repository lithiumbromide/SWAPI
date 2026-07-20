---
title: "swFeatureTreeFolderType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFeatureTreeFolderType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureTreeFolderType_e.html"
---

# swFeatureTreeFolderType_e Enumeration

Ways to insert feature folders for selected features or components in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFeatureTreeFolderType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFeatureTreeFolderType_e
```

### C#

```csharp
public enum swFeatureTreeFolderType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFeatureTreeFolderType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFeatureTreeFolder_Containing | 2 = Create and insert a folder to contain the pre-selected features |
| swFeatureTreeFolder_EmptyBefore | 1 = Create and insert an empty folder before the pre-selected features |
| swFeatureTreeFolder_Mold | 3 = Create and insert a Surface Bodies folder containing three folders: Cavity Surface Bodies, Core Surface Bodies, and Parting Surface Bodies for a pre-selected surface feature |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
