---
title: "DModelViewEvents_DisplayModeChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_DisplayModeChangePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DisplayModeChangePostNotifyEventHandler.html"
---

# DModelViewEvents_DisplayModeChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a model view display mode is changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_DisplayModeChangePostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_DisplayModeChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_DisplayModeChangePostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_DisplayModeChangePostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DisplayModeChangePostNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~DisplayModeChangePostNotify_EV.html).

## Examples

Contact SOLIDWORKS API Support to obtain **Event Monitor for SOLIDWORKS 2012 (VBA)**.

## Remarks

This event occurs after the display mode has been changed using [IModelDocExtension::DisplayMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayMode.html).

If developing a C++ application, use [swViewDisplayModeChangePostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
