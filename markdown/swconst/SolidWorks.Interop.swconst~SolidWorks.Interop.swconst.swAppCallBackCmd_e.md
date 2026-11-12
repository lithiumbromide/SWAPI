---
title: "swAppCallBackCmd_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAppCallBackCmd_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppCallBackCmd_e.html"
---

# swAppCallBackCmd_e Enumeration

Types of application callback functions.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAppCallBackCmd_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAppCallBackCmd_e
```

### C#

```csharp
public enum swAppCallBackCmd_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAppCallBackCmd_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAppHelpContext | 3 = Not used |
| swAppIsCmdEnabled | 4 = CommandGroup item is enabled |
| swAppIsNewCmd | 1 = True if data is new, false if not |
| swAppPostNotifyEvent | 5 = Your application is posting a callback to the SOLIDWORKS message queue that will be invoked when the callback is processed in the SOLIDWORKS message queue |
| swAppWhatsNewDescription | 2 = Interactive What's New |

## Remarks

Use with [ISldWorks::AddCallback](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddCallback.html).

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
