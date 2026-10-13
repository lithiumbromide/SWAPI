---
title: "DPartDocEvents_DeleteSelectionPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DeleteSelectionPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteSelectionPreNotifyEventHandler.html"
---

# DPartDocEvents_DeleteSelectionPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user when the selection is deleted.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DeleteSelectionPreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DeleteSelectionPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DeleteSelectionPreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DeleteSelectionPreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DeleteSelectionPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~DeleteSelectionPreNotify_EV.html).

## Remarks

Returning S_false from your notification handler prevents deletion of the selected item.

If developing a COM application, use [swPartDeleteSelectionPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
