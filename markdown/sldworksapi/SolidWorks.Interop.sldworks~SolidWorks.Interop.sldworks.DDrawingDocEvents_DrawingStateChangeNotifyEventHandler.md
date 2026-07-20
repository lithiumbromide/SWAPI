---
title: "DDrawingDocEvents_DrawingStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_DrawingStateChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DrawingStateChangeNotifyEventHandler.html"
---

# DDrawingDocEvents_DrawingStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a drawing's state changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_DrawingStateChangeNotifyEventHandler( _
   ByVal PreviousState As System.Short, _
   ByVal newState As System.Short _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_DrawingStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_DrawingStateChangeNotifyEventHandler(
   System.short PreviousState,
   System.short newState
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_DrawingStateChangeNotifyEventHandler(
   System.short PreviousState,
   System.short newState
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `PreviousState`: Previous state as defined by

[swDrawingMode_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDrawingMode_e.html)
- `newState`: New state as defined by swDrawingMode_e

## VBA Syntax

See

[DrawingStateChangeNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~DrawingStateChangeNotify_EV.html)

.

## Remarks

If developing a C++ application, use

[swDrawingDrawingStateChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html)

to register for this notification.

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
