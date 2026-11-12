---
title: "DModelViewEvents_GraphicsRenderPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_GraphicsRenderPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_GraphicsRenderPostNotifyEventHandler.html"
---

# DModelViewEvents_GraphicsRenderPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after all SOLIDWORKS graphics are drawn, including SOLIDWORKS model, sketch, dimension, and annotation graphics.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_GraphicsRenderPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_GraphicsRenderPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_GraphicsRenderPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_GraphicsRenderPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [GraphicsRenderPostNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~GraphicsRenderPostNotify_EV.html).

## Remarks

This event:

- is always fired after rendering to Layer2. Depending on optimization:

  - [RenderLayer0Notify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_RenderLayer0NotifyEventHandler.html) is fired when SOLIDWORKS renders to Layer0.
  - [BufferSwapNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.html) is fired after rendering to Layer0**.**
- allows third-party applications to draw graphics in the SOLIDWORKS model window without worrying about SOLIDWORKS graphics being drawn over them.
- does not support depth buffering.

If developing a C++ application, use [swViewGraphicsRenderPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
