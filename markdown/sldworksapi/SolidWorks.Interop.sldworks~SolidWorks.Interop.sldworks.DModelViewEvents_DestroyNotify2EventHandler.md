---
title: "DModelViewEvents_DestroyNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_DestroyNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DestroyNotify2EventHandler.html"
---

# DModelViewEvents_DestroyNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a model view is about to be destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_DestroyNotify2EventHandler( _
   ByVal DestroyType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_DestroyNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_DestroyNotify2EventHandler(
   System.int DestroyType
)
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_DestroyNotify2EventHandler(
   System.int DestroyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DestroyType`: Value as defined by [swDestroyNotifyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDestroyNotifyType_e.html)

## VBA Syntax

See [DestroyNotify2 Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~DestroyNotify2_EV.html).

## Remarks

This event is sent when a view is being destroyed and will no longer be available to the end-user. In this case, the destroyType value is swDestroyNotifyDestroy.

This event is also sent for each view of a model when the document is closed, yet the view is not destroyed. This can happen when the model is being used by an open assembly or drawing document. In this case, the destroyType value is swDestroyNotifyHidden. This indicates that the view is still available for use, but is not visible.

If the part is then reopened, a IPartDoc [ViewNewNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ViewNewNotify2EventHandler.html) event is again sent for all views in the part. At this point, you can recreate your link to these views, or if your application did not destroy the views, you can recognize that these views are no longer hidden. When the document and all referencing assemblies and drawings are finally closed, then the views are destroyed and this event is sent for each of the model views, with the destroyType = swDestroyNotifyDestroy.

If developing a C++ application, use [swViewDestroyNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
