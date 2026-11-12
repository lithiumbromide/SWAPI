---
title: "DPartDocEvents_ModifyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ModifyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ModifyNotifyEventHandler.html"
---

# DPartDocEvents_ModifyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when a document is marked as dirty for the first time.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ModifyNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ModifyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ModifyNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ModifyNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModifyNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ModifyNotify_EV.html).

## Remarks

If the user saves the document in the current SOLIDWORKS Design session, then the event is fired when the document is marked dirty again.

If developing a C++ application, use [swPartModifyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
