---
title: "swChildComponentInBOMOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swChildComponentInBOMOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChildComponentInBOMOption_e.html"
---

# swChildComponentInBOMOption_e Enumeration

Child component display options in Bills of Materials (BOM) for assemblies and for parts that have weldment/sheet metal cut lists.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swChildComponentInBOMOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swChildComponentInBOMOption_e
```

### C#

```csharp
public enum swChildComponentInBOMOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swChildComponentInBOMOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swChildComponent_Hide | 1 = Child components might be listed individually, depending on the properties that you selected when you created the BOM |
| swChildComponent_Promote | 3 = The model's configuration dissolves when it appears in a BOM; all of its child components are promoted one level |
| swChildComponent_Show | 2 = Child components appear as single items in the BOM |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
