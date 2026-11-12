---
title: "DModelViewEvents_RepaintNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_RepaintNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RepaintNotifyEventHandler.html"
---

# DModelViewEvents_RepaintNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a view is about to be repainted and returns the paint type.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_RepaintNotifyEventHandler( _
   ByVal paintType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_RepaintNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_RepaintNotifyEventHandler(
   System.int paintType
)
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_RepaintNotifyEventHandler(
   System.int paintType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `paintType`: Valid paint type as defined in [swRepaintTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRepaintTypes_e.html) (only the first two types are supported)

## VBA Syntax

See [RepaintNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~RepaintNotify_EV.html).

## Remarks

Returns S_false to stop from proceeding with the action that caused the notification. This also prevents sending the IModelView [BufferSwapNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.html) event.

If developing a C++ application, use [swViewBufferSwapNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SoidWorks 2001Plus FCS, Revision Number 10.0
