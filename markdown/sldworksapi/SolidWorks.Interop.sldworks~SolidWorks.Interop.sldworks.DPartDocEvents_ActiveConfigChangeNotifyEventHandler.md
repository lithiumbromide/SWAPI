---
title: "DPartDocEvents_ActiveConfigChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ActiveConfigChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveConfigChangeNotifyEventHandler.html"
---

# DPartDocEvents_ActiveConfigChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired with the user switches to a different configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ActiveConfigChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ActiveConfigChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ActiveConfigChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ActiveConfigChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveConfigChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ActiveConfigChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartActiveConfigChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
