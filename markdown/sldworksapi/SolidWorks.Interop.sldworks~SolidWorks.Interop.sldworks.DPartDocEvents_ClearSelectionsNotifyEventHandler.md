---
title: "DPartDocEvents_ClearSelectionsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ClearSelectionsNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ClearSelectionsNotifyEventHandler.html"
---

# DPartDocEvents_ClearSelectionsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when selections are cleared using Clear Selections.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ClearSelectionsNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ClearSelectionsNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ClearSelectionsNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ClearSelectionsNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ClearSelectionsNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ClearSelectionsNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartClearSelectionsNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this event.

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
