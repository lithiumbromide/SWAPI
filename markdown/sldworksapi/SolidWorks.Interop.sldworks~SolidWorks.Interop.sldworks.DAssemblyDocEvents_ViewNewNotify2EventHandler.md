---
title: "DAssemblyDocEvents_ViewNewNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ViewNewNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ViewNewNotify2EventHandler.html"
---

# DAssemblyDocEvents_ViewNewNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a new view model window has been created.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ViewNewNotify2EventHandler( _
   ByVal viewBeingAdded As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ViewNewNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ViewNewNotify2EventHandler(
   System.object viewBeingAdded
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ViewNewNotify2EventHandler(
   System.Object^ viewBeingAdded
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `viewBeingAdded`: New [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) window

## VBA Syntax

See [ViewNewNotify2 Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ViewNewNotify2_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyViewNewNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This event is sent for each new model view created by the window splitter bar. It is also sent for each new model view created in a document when Window, New Window is selected. A Dispatch pointer to the new model view is passed, which can be used to register for [IModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) events or to run the various ModelView APIs such as [IModelView::GetViewHWnd](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetViewHWnd.html).

Because [FileOpenNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html) and [FileNewNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler.html) are post-notifications, SOLIDWORKS Design has already constructed the model views and has already fired this event by the time your application receives FileOpenNotify2 or FileNewNotify2. Therefore, within your functions that handle FileOpenNotify2 and FileNewNotify2, you should programmatically traverse each model view in the newly opened or created document ([IModelDoc2::EnumModelViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EnumModelViews.html) or [IModelDoc2::GetFirstModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetFirstModelView.html) or [IModelDoc2::IGetFirstModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetFirstModelView.html) and [IModelView::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetNext.html) or [IModelView::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGetNext.html)), and register each view for ModelView events.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
