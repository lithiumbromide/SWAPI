---
title: "swLinkBomToDisplayStateError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swLinkBomToDisplayStateError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLinkBomToDisplayStateError_e.html"
---

# swLinkBomToDisplayStateError_e Enumeration

Errors when linking a BOM to a Display State.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swLinkBomToDisplayStateError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swLinkBomToDisplayStateError_e
```

### C#

```csharp
public enum swLinkBomToDisplayStateError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swLinkBomToDisplayStateError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swLinkBomToDisplayState_InvalidDisplayState | 1 |
| swLinkBomToDisplayState_MultipleConfigurations | 2 |
| swLinkBomToDisplayState_Success | 0 |

## Remarks

This enumeration is used in IBomFeature::GetLinkToDisplayState and IBomFeature::SetLinkToDisplayState.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
