---
title: "DPartDocEvents_NewSelectionNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_NewSelectionNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_NewSelectionNotifyEventHandler.html"
---

# DPartDocEvents_NewSelectionNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the selection list has changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_NewSelectionNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_NewSelectionNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_NewSelectionNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_NewSelectionNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [NewSelectionNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~NewSelectionNotify_EV.html).

## Remarks

This notification is generated when items are added, removed, or reordered in the selection list.

If developing a C++ application, use [swPartNewSelectionNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
