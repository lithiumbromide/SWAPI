---
title: "swAddComponentConfigOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAddComponentConfigOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddComponentConfigOptions_e.html"
---

# swAddComponentConfigOptions_e Enumeration

Options for adding components to an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAddComponentConfigOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAddComponentConfigOptions_e
```

### C#

```csharp
public enum swAddComponentConfigOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAddComponentConfigOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAddComponentConfigOptions_CurrentSelectedConfig | 0 = Add a part or assembly in its last saved configuration. (See IAssemblyDoc::AddComponent5 ) |
| swAddComponentConfigOptions_NewConfigWithAllReferenceModels | 1 = Add an assembly with all of its components resolved. (See IAssemblyDoc::AddComponent5) |
| swAddComponentConfigOptions_NewConfigWithAsmStructure | 2 = Add an assembly with all of its components suppressed. (See IAssemblyDoc::AddComponent5) |

## Examples

[Add Component and Mate (VBA)](ms-its:sldworksapi.chm::/Add_Component_and_Mate_Example_VB.htm)
[Add Component and Mate (VB.NET)](ms-its:sldworksapi.chm::/Add_Component_and_Mate_Example_VBNET.htm)
[Add Component and Mate (C#)](ms-its:sldworksapi.chm::/Add_Component_and_Mate_Example_CSharp.htm)

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
