---
title: "swFeatureEditStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFeatureEditStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureEditStatus_e.html"
---

# swFeatureEditStatus_e Enumeration

Editing status of feature. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFeatureEditStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFeatureEditStatus_e
```

### C#

```csharp
public enum swFeatureEditStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFeatureEditStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFeature_Editable | 0 or 0x0; Feature can be edited |
| swFeature_NonEditable | 1 or 0x1; Feature cannot be edited |
| swFeature_UnderEditing | 2 or 0x2; If the feature is a sketch, then the sketch is already being edited |

## Remarks

Although swFeatureEditStatus_e is a bitmask, you currently cannot combine its mutually exclusive enumerators.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
