---
title: "swBOMPartNumberSource_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBOMPartNumberSource_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMPartNumberSource_e.html"
---

# swBOMPartNumberSource_e Enumeration

Sources from numbers in BOM tables. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBOMPartNumberSource_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBOMPartNumberSource_e
```

### C#

```csharp
public enum swBOMPartNumberSource_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBOMPartNumberSource_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBOMPartNumber_ConfigurationName | 2 or 0x2 |
| swBOMPartNumber_DocumentName | 1 or 0x1 |
| swBOMPartNumber_ParentName | 4 or 0x4 |
| swBOMPartNumber_UserSpecified | 8 or 0x8 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
