---
title: "DDrawingDocEvents_ViewPositionChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_ViewPositionChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ViewPositionChangeNotifyEventHandler.html"
---

# DDrawingDocEvents_ViewPositionChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a drawing view changes position.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_ViewPositionChangeNotifyEventHandler( _
   ByVal ViewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_ViewPositionChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_ViewPositionChangeNotifyEventHandler(
   System.string ViewName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_ViewPositionChangeNotifyEventHandler(
   System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Name of the drawing view whose position changed

## VBA Syntax

See [ViewPositionChange Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~ViewPositionChange_EV.html).

## Remarks

The event is fired whenever a drawing view is moved. If MoveChildViews is true in [IView::SetViewPostion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetViewPosition.html), an event is also fired when each child view is moved.

If developing a C++ application, use [swDrawingViewPositionChange](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
