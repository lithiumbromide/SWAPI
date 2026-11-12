---
title: "DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler.html"
---

# DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when the selection is deleted.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DeleteSelectionPreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~DeleteSelectionPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyDeleteSelectionPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Returning S_false from your notification handler prevents deletion of the selected item.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
