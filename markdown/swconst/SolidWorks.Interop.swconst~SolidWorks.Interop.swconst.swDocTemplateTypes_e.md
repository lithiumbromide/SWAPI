---
title: "swDocTemplateTypes_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDocTemplateTypes_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDocTemplateTypes_e.html"
---

# swDocTemplateTypes_e Enumeration

Document template types. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDocTemplateTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDocTemplateTypes_e
```

### C#

```csharp
public enum swDocTemplateTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDocTemplateTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDocTemplateTypeASSEMBLY | 4 or 0x4 |
| swDocTemplateTypeDRAWING | 8 or 0x8 |
| swDocTemplateTypeInContext | 16 or 0x10 |
| swDocTemplateTypeNONE | 1 or 0x1 |
| swDocTemplateTypePART | 2 or 0x2 |

## Remarks

These values can be OR'd together to indicate on which toolbar the document types should reside.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
