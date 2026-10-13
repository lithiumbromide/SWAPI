---
title: "DAssemblyDocEvents_FlipLoopNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FlipLoopNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FlipLoopNotifyEventHandler.html"
---

# DAssemblyDocEvents_FlipLoopNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies your program when a loop flips.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FlipLoopNotifyEventHandler( _
   ByVal TheLoop As System.Object, _
   ByVal TheEdge As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FlipLoopNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FlipLoopNotifyEventHandler(
   System.object TheLoop,
   System.object TheEdge
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FlipLoopNotifyEventHandler(
   System.Object^ TheLoop,
   System.Object^ TheEdge
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TheLoop`: [Loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) that was flipped
- `TheEdge`: [Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) about which the loop was flipped

## VBA Syntax

See [FlipLoopNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FlipLoopNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFlipLoopNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
