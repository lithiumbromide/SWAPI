---
title: "DModelViewEvents_UserClearSelectionsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_UserClearSelectionsNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_UserClearSelectionsNotifyEventHandler.html"
---

# DModelViewEvents_UserClearSelectionsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a user:

1. Clicks the right-mouse button when the pointer is over a selection box on a PropertyManager page.
2. Selects Clear Selections on the short-cut menu.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_UserClearSelectionsNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_UserClearSelectionsNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_UserClearSelectionsNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_UserClearSelectionsNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [UserClearSelectionsNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~UserClearSelectionsNotify_EV.html).

## Remarks

If developing a C++ application, use [swViewUserClearSelectionsNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
