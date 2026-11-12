---
title: "swConfigurationChangeTypes_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swConfigurationChangeTypes_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigurationChangeTypes_e.html"
---

# swConfigurationChangeTypes_e Enumeration

Types of configuration changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swConfigurationChangeTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swConfigurationChangeTypes_e
```

### C#

```csharp
public enum swConfigurationChangeTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swConfigurationChangeTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swConfigurationChangeTypes_AddChildConfiguration | 2 |
| swConfigurationChangeTypes_AddDisplayState | 6 |
| swConfigurationChangeTypes_ChangeRepresentationParent | 14 |
| swConfigurationChangeTypes_ComponentVisibilityState | 4 |
| swConfigurationChangeTypes_ConvertToPhysicalProduct | 13 = Change to Physical Product for SOLIDWORKS Design connected to the 3DEXPERIENCE platform only; used in DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler |
| swConfigurationChangeTypes_ConvertToRepresentation | 12 = Change to Representation for SOLIDWORKS Design connected to the 3DEXPERIENCE platform only; used in DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler |
| swConfigurationChangeTypes_CustomProperty | 5 |
| swConfigurationChangeTypes_DimensionValue | 0 |
| swConfigurationChangeTypes_Feature | 9 |
| swConfigurationChangeTypes_RemoveChildConfiguration | 3 |
| swConfigurationChangeTypes_RemoveDisplayState | 7 |
| swConfigurationChangeTypes_RenameDisplayState | 8 |
| swConfigurationChangeTypes_SuppressionState | 1 |
| swConfigurationChangeTypes_Undefined | -1 |
| swConfigurationChangeTypes_Unused1 | 10 = Not used |
| swConfigurationChangeTypes_Unused2 | 11 = Not used |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
