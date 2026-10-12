---
title: "DSldWorksEvents_ActiveDocChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_ActiveDocChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler.html"
---

# DSldWorksEvents_ActiveDocChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the active window has changed. This change can be between windows of the same document or between windows of different documents.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_ActiveDocChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_ActiveDocChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_ActiveDocChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_ActiveDocChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveDocChangeNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~ActiveDocChangeNotify_EV.html).

## Remarks

For example, if you open two documents and then select Window, New Window for one of the documents, you will have three windows visible in your SOLIDWORKS session. This event is sent when you switch between any combination of those windows.

This event is only sent when the active window in the SOLIDWORKS session actually changes to a new active window. Window activations are not guaranteed during, for example, the shutdown of the SOLIDWORKS application. For example, if the SOLIDWORKS application closes a non-active document, then there re is no need to activate a new window.

If developing a C++ application, use [swAppDocChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
