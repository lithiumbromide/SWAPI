---
title: "swFileSaveWarning_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFileSaveWarning_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileSaveWarning_e.html"
---

# swFileSaveWarning_e Enumeration

Values for File, Save warnings that can be returned from the [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) Save methods. These warnings do not cause the File, Save operation to fail. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFileSaveWarning_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFileSaveWarning_e
```

### C#

```csharp
public enum swFileSaveWarning_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFileSaveWarning_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFileSaveWarning_AnimatorCameraViews | 128 or 0x80 |
| swFileSaveWarning_AnimatorFeatureEdits | 16 or 0x10 |
| swFileSaveWarning_AnimatorLightEdits | 64 or 0x40 |
| swFileSaveWarning_AnimatorNeedToSolve | 8 or 0x8 |
| swFileSaveWarning_AnimatorSectionViews | 256 or 0x100 |
| swFileSaveWarning_EdrwingsBadSelection | 32 or 0x20 |
| swFileSaveWarning_MissingOLEObjects | 512 or 0x200 |
| swFileSaveWarning_NeedsRebuild | 2 or 0x2 |
| swFileSaveWarning_OpenedViewOnly | 1024 or 0x400 |
| swFileSaveWarning_RebuildError | 1 or 0x1 |
| swFileSaveWarning_ViewsNeedUpdate | 4 or 0x4 |
| swFileSaveWarning_XmlInvalid | 2048 or 0x800 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
