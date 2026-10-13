---
title: "DPartDocEvents_FlipLoopNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FlipLoopNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FlipLoopNotifyEventHandler.html"
---

# DPartDocEvents_FlipLoopNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a loop is flipped.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FlipLoopNotifyEventHandler( _
   ByVal TheLoop As System.Object, _
   ByVal TheEdge As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FlipLoopNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FlipLoopNotifyEventHandler(
   System.object TheLoop,
   System.object TheEdge
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FlipLoopNotifyEventHandler(
   System.Object^ TheLoop,
   System.Object^ TheEdge
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TheLoop`: [Loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) that was flipped
- `TheEdge`: [Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) about which the loop was flipped

## VBA Syntax

See [FlipLoopNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FlipLoopNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFlipLoopNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
