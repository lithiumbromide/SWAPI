---
title: "DDrawingDocEvents_ViewCreatePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_ViewCreatePreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ViewCreatePreNotifyEventHandler.html"
---

# DDrawingDocEvents_ViewCreatePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user application when a drawing view is about to be created.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_ViewCreatePreNotifyEventHandler( _
   ByVal modelDocBeingAdded As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_ViewCreatePreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_ViewCreatePreNotifyEventHandler(
   System.object modelDocBeingAdded
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_ViewCreatePreNotifyEventHandler(
   System.Object^ modelDocBeingAdded
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `modelDocBeingAdded`: [Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) used to create the drawing view

## VBA Syntax

See [ViewCreatePreNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~ViewCreatePreNotify_EV.html).

## Remarks

This notification occurs just before the drawing view is added as a feature to the drawing document. Use [IModelDoc2::GetPathName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) and [IConfigurationManager::ActiveConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html) to get the model document's path, filename, and configuration to use to create the drawing view.

This notification also gets fired for empty drawing views. Because empty drawing views do not have a model document, the argument ModelDocBeingAdded is NULL or Nothing. Use the event handler to check ModelDocBeingAdded for NULL or Nothing before using this notification.

If developing a C++ application, then use [swDrawingViewCreatePreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
