---
title: "DModelViewEvents_DisplayModeChangePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_DisplayModeChangePreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DisplayModeChangePreNotifyEventHandler.html"
---

# DModelViewEvents_DisplayModeChangePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a model view display mode is about to be changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_DisplayModeChangePreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_DisplayModeChangePreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_DisplayModeChangePreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_DisplayModeChangePreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DisplayModeChangePreNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~DisplayModeChangePreNotify_EV.html).

## Examples

Contact SOLIDWORKS API Support to obtain **Event Monitor for SOLIDWORKS 2012 (VBA)**.

## Remarks

This event occurs when the display mode is about to be changed using [IModelDocExtension::DisplayMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayMode.html).

If developing a C++ application, use [swViewDisplayModeChangePreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
