---
title: "DSldWorksEvents_OnIdleNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_OnIdleNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_OnIdleNotifyEventHandler.html"
---

# DSldWorksEvents_OnIdleNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after all of the messages have been processed, included posted repaints; therefore, eliminating the need to call [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_OnIdleNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_OnIdleNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_OnIdleNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_OnIdleNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [OnIdleNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~OnIdleNotify_EV.html).

## Remarks

If developing a C++ application, use [swAppOnIdleNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
