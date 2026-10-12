---
title: "DSldWorksEvents_DestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_DestroyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DestroyNotifyEventHandler.html"
---

# DSldWorksEvents_DestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Sent to an MFC-based or a COM-based DLL add-in when the SOLIDWORKS session is about to be destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_DestroyNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_DestroyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_DestroyNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_DestroyNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DestroyNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~DestroyNotify_EV.html).

## Remarks

This is a pre-notification. Add-ins should not perform any cleanup inside this event.

Use [ISwAddin::DisconnectFromSw](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~DisconnectFromSW.html) to perform any cleanup of COM-based DLL add-ins.

If developing a C++ application, use [swAppDestroyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
