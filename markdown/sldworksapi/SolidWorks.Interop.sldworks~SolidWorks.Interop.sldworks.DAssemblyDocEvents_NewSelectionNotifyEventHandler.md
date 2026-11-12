---
title: "DAssemblyDocEvents_NewSelectionNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_NewSelectionNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_NewSelectionNotifyEventHandler.html"
---

# DAssemblyDocEvents_NewSelectionNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the selection list has changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_NewSelectionNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_NewSelectionNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_NewSelectionNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_NewSelectionNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [NewSelectionNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~NewSelectionNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyNewSelectionNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This notification is generated when items are added, removed, or reordered in the selection list.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
