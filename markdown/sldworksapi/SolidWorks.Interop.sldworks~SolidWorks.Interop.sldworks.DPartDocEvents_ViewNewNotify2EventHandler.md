---
title: "DPartDocEvents_ViewNewNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ViewNewNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ViewNewNotify2EventHandler.html"
---

# DPartDocEvents_ViewNewNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a new model view window is created. For example, this event is sent for each new model view created by the window split bar.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ViewNewNotify2EventHandler( _
   ByVal viewBeingAdded As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ViewNewNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ViewNewNotify2EventHandler(
   System.object viewBeingAdded
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ViewNewNotify2EventHandler(
   System.Object^ viewBeingAdded
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `viewBeingAdded`: New window view

## VBA Syntax

See [ViewNewNotify2 Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ViewNewNotify2_EV.html).

## Remarks

SOLIDWORKS generates this notification when the user selects Window, New Window, or uses the splitter and clicks in the new view.

SOLIDWORKS passes a Dispatch pointer to the new view, which you can use to register for [IModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) events or to run IModelView functions, such as [IModelView::GetViewHWnd](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetViewHWnd.html).

Since the SOLIDWORKS events [FileOpenNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html) and [FileNewNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler.html) are post-notifications, SOLIDWORKS has already constructed the views and has already generated this event by the time your application receives FileOpenNotify2 or FileNewNotify2. Therefore, within your functions that handle FileOpenNotify2 and FileNewNotify2, you should programmatically traverse each view in the newly opened or created document ([IEnumModelViews::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumModelViews~Next.html) or [IModelDoc2::GetFirstModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetFirstModelView.html) or [IModelDoc2::IGetFirstModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetFirstModelView.html) or [IModelView::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetNext.html) or [IModelView::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGetNext.html)), and register each view for IModelView events.

The difference between [ViewNewNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ViewNewNotifyEventHandler.html) and ViewNewNotify2 is that ViewNewNotify is sent only when the view is activated for the first time. With ViewNewNotify2, the notification is sent whenever a new view is initialized and available for use by the third-party application. The view does not need to be activated by the user for the event to be sent.

If developing a C++ application, use [swPartViewNewNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
