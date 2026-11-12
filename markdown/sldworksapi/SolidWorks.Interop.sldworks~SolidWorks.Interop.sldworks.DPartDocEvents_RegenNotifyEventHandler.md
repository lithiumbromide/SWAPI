---
title: "DPartDocEvents_RegenNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_RegenNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RegenNotifyEventHandler.html"
---

# DPartDocEvents_RegenNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a part document is about to be rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_RegenNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_RegenNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_RegenNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_RegenNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RegenNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~RegenNotify_EV.html).

## Remarks

You can also use [IModelDoc2::GetUpdateStamp](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUpdateStamp.html) to determine when changes have taken place in this document.

Return S_FALSE to stop from proceeding with the action that caused the notification.

If developing a C++ application, use [swPartRegenNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
