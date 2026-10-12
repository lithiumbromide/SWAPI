---
title: "swGetOpenFileNameOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swGetOpenFileNameOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGetOpenFileNameOptions_e.html"
---

# swGetOpenFileNameOptions_e Enumeration

Options for opening a file returned by [ISldWorks::GetOpenFileName2](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName2.html). [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swGetOpenFileNameOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swGetOpenFileNameOptions_e
```

### C#

```csharp
public enum swGetOpenFileNameOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swGetOpenFileNameOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swGetOpenFileNameOptions_AdvancedConfig | 0x2000; "<Advanced>" selected in configuration dropdown |
| swGetOpenFileNameOptions_AutoMissingConfig | 0x20; Reserved for internal use |
| swGetOpenFileNameOptions_DontLoadHiddenComponents | 0x100; Does not load hidden components (assemblies only) |
| swGetOpenFileNameOptions_LDR_EditAssembly | 0x800; Reserved for internal use |
| swGetOpenFileNameOptions_LoadExternalReferencesInMemory | 0x200; Reserved for internal use |
| swGetOpenFileNameOptions_LoadLightweight | 0x80; Opens the document in lightweight mode |
| swGetOpenFileNameOptions_LoadModel | 0x10; Reserved for internal use |
| swGetOpenFileNameOptions_OpenDetailingMode | 0x400; Opens the document in detailing mode without part and assembly data (drawings only) |
| swGetOpenFileNameOptions_OverrideDefaultLoadLightweight | 0x40; Reserved for internal use |
| swGetOpenFileNameOptions_RapidDraft | 0x8; Reserved for internal use |
| swGetOpenFileNameOptions_ReadOnly | 0x2; Opens the document read only |
| swGetOpenFileNameOptions_SelectedSheets | 0x8000; "Selected" is checked in Select Sheet to load dialog |
| swGetOpenFileNameOptions_Silent | 0x1; Reserved for internal use |
| swGetOpenFileNameOptions_SpeedPak | 0x1000; Uses Speedpak (assemblies only) |
| swGetOpenFileNameOptions_UseLargeAssemblySettings | 0x4000; Uses large assembly settings (assemblies only) |
| swGetOpenFileNameOptions_ViewOnly | 0x4; Opens the document view only; returned if "None" is selected in Select Sheet to load dialog |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
