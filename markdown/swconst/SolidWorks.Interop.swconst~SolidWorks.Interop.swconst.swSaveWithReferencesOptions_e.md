---
title: "swSaveWithReferencesOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSaveWithReferencesOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveWithReferencesOptions_e.html"
---

# swSaveWithReferencesOptions_e Enumeration

Options for saving references while getting the [IAdvancedSaveAsOptions](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html) object; used by the Options parameter of [IModelDocExtension::GetAdvancedSaveAsOptions](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions.html). [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSaveWithReferencesOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSaveWithReferencesOptions_e
```

### C#

```csharp
public enum swSaveWithReferencesOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSaveWithReferencesOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSaveWithReferencesOptions_IncludeBrokenReferences | 4 = Reference list contains both normal references and components with broken references |
| swSaveWithReferencesOptions_IncludeToolBoxParts | 2 = Reference list contains both normal and ToolBox references |
| swSaveWithReferencesOptions_IncludeVirtualComponents | 1 = Reference list contains both normal and virtual component references |
| swSaveWithReferencesOptions_None | 0 = Reference list contains only normal references |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
