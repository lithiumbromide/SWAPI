---
title: "DModelViewEvents_RepaintPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_RepaintPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RepaintPostNotifyEventHandler.html"
---

# DModelViewEvents_RepaintPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a view has been repainted.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_RepaintPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_RepaintPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_RepaintPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_RepaintPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RepaintPostNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~RepaintPostNotify_EV.html).

## Remarks

If developing a C++ application, use [swViewRepaintPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
