---
title: "swManipulatorOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swManipulatorOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swManipulatorOptions_e.html"
---

# swManipulatorOptions_e Enumeration

Manipulator options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swManipulatorOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swManipulatorOptions_e
```

### C#

```csharp
public enum swManipulatorOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swManipulatorOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swManipulatorOpts_Default | 0 or 0x0; Manipulators created using the SOLIDWORKS API are deleted when a component is modified or deleted in the context of an assembly NOTE: This is the default behavior. |
| swManipulatorOpts_KeepAfterComponentModify | 1 or 0x1; Manipulators are not deleted when a component is modified or deleted in the context of an assembly |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
