---
title: "DPartDocEvents_ActiveConfigChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ActiveConfigChangePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveConfigChangePostNotifyEventHandler.html"
---

# DPartDocEvents_ActiveConfigChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the user has switched to a different configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ActiveConfigChangePostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ActiveConfigChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ActiveConfigChangePostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ActiveConfigChangePostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveConfigChangePostNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ActiveConfigChangePostNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartConfigChangePostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
