---
title: "DAssemblyDocEvents_RegenNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_RegenNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenNotifyEventHandler.html"
---

# DAssemblyDocEvents_RegenNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when an assembly document is about to be rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_RegenNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_RegenNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_RegenNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_RegenNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RegenNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~RegenNotify_EV.html).

## Examples

[Fire Assembly Rebuild Events (C#)](Regen_Post_Notify2_Event_Handler_Example_CSharp.htm)
[Fire Assembly Rebuild Events (VB.NET)](Regen_Post_Notify2_Event_Handler_Example_VBNET.htm)
[Fire Assembly Rebuild Events (VBA)](Regen_Post_Notify2_Event_Handler_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyRegenNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Use [DAssemblyDocEvents RegenPostNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotify2EventHandler.html) to fire an event after the assembly is rebuilt.

You can also use [IModelDoc2::GetUpdateStamp](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUpdateStamp.html) to determine when changes take place in this document.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
