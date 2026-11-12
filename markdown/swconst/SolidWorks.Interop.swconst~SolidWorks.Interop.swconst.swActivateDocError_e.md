---
title: "swActivateDocError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swActivateDocError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swActivateDocError_e.html"
---

# swActivateDocError_e Enumeration

Document activation errors. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swActivateDocError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swActivateDocError_e
```

### C#

```csharp
public enum swActivateDocError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swActivateDocError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDocNeedsRebuildWarning | 2 or 0x2; The document that was activated needs to be rebuilt (your application can use EditRebuild on the PartDoc, AssemblyDoc, or DrawingDoc to perform the rebuild). |
| swGenericActivateError | 1 or 0x1; An unspecified error was encountered, and the document was not activated. |

## Remarks

Bitmask

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
