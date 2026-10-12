---
title: "DPartDocEvents_DestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DestroyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DestroyNotifyEventHandler.html"
---

# DPartDocEvents_DestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DPartDocEvents_DestroyNotify2EventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DestroyNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DestroyNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DestroyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DestroyNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DestroyNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DestroyNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~DestroyNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartDestroyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
