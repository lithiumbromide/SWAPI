---
title: "swFileCloseNotifyReason_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFileCloseNotifyReason_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileCloseNotifyReason_e.html"
---

# swFileCloseNotifyReason_e Enumeration

Reasons for the [FileCloseNotify](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileCloseNotifyEventHandler.html) event.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFileCloseNotifyReason_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFileCloseNotifyReason_e
```

### C#

```csharp
public enum swFileCloseNotifyReason_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFileCloseNotifyReason_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFileCloseNotifyReason_CloseForReload | 1 = ISldWorks::CloseAndReopen was called |
| swFileCloseNotifyReason_Unknown | 0 = unknown reason |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
