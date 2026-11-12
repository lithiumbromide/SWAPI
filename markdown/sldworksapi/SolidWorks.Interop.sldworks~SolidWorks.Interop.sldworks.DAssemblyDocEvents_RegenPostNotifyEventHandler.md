---
title: "DAssemblyDocEvents_RegenPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_RegenPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotifyEventHandler.html"
---

# DAssemblyDocEvents_RegenPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DAssemblyDocEvents RegenPostNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_RegenPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_RegenPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_RegenPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_RegenPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RegenPostNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~RegenPostNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyRegenPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

You can also use [IModelDoc2::GetUpdateStamp](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUpdateStamp.html) to determine when changes take place in this document.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
