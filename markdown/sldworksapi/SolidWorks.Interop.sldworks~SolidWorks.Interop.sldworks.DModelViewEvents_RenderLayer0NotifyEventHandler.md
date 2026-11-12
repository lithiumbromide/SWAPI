---
title: "DModelViewEvents_RenderLayer0NotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_RenderLayer0NotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RenderLayer0NotifyEventHandler.html"
---

# DModelViewEvents_RenderLayer0NotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired whenever SOLIDWORKS renders to Layer0.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_RenderLayer0NotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_RenderLayer0NotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_RenderLayer0NotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_RenderLayer0NotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RenderLayer0Notify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~RenderLayer0Notify_EV.html).

## Remarks

This event allows you to render the model instead of SOLIDWORKS rendering the model. If the return value from the event is S_FALSE, then SOLIDWORKS will not render to Layer0, but will render to Layer1.

**NOTE:** When SOLIDWORKS renders to a frame, it renders two layers:

This event is not sent if [swViewRepaintNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) returns S_FALSE. Also, if [swViewRenderLayer0Notify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) returns S_FALSE, then [swViewBufferSwapNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) is not sent.

[BufferSwapNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.html) is fired after rendering to Layer0, depending on optimization**.** [GraphicsRenderPostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_GraphicsRenderPostNotifyEventHandler.html) is always fired after rendering to Layer2.

Prior to the event, the graphics area is cleared and the model view's xform is set.

If developing a C++ application, use [swViewRenderLayer0Notify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
