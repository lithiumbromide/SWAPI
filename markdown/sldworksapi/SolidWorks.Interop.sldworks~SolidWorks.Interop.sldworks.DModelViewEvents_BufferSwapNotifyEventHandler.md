---
title: "DModelViewEvents_BufferSwapNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_BufferSwapNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.html"
---

# DModelViewEvents_BufferSwapNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired from the model view immediately before the buffers are swapped when rendering shaded graphics in OpenGL.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_BufferSwapNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_BufferSwapNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_BufferSwapNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_BufferSwapNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [BufferSwapNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~BufferSwapNotify_EV.html).

## Remarks

The OpenGL context contains matrices such that graphics are drawn correctly relative to the part or top-level assembly, but not any components within the assembly. This event is also sent when the model is in HLR or HLV mode and being dynamically rotated.

This event is sent for any other wireframe repainting. (GDI is used for all other wireframe painting). You can determine if a model is shaded by using [IModelView::GetDisplayState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetDisplayState.html).

This event is fired after rendering to Layer0.

**NOTE:** When SOLIDWORKS renders to a frame, it renders two layers:

[RenderLayer0Notify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_RenderLayer0NotifyEventHandler.html) is fired when SOLIDWORKS renders to Layer0, depending on optimization. [GraphicsRenderPostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_GraphicsRenderPostNotifyEventHandler.html) is always fired after rendering to Layer2.

If developing a C++ application, use [swViewBufferSwapNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
