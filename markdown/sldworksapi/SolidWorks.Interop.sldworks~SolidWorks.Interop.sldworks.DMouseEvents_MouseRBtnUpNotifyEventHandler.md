---
title: "DMouseEvents_MouseRBtnUpNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DMouseEvents_MouseRBtnUpNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseRBtnUpNotifyEventHandler.html"
---

# DMouseEvents_MouseRBtnUpNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the right-mouse button is released after being pressed down.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMouseEvents_MouseRBtnUpNotifyEventHandler( _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal WParam As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMouseEvents_MouseRBtnUpNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMouseEvents_MouseRBtnUpNotifyEventHandler(
   System.int X,
   System.int Y,
   System.int WParam
)
```

### C++/CLI

```cpp
public delegate System.int DMouseEvents_MouseRBtnUpNotifyEventHandler(
   System.int X,
   System.int Y,
   System.int WParam
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate of the pointer in the window space
- `Y`: y coordinate of the pointer in the window space
- `WParam`: Data about the state of the keyboard at the time the event was sent; see MSDN for details on how to decode this data

## VBA Syntax

See [MouseRBtnUpNotify Event (Mouse)](ms-its:sldworksapivb6.chm::/SldWorks~Mouse~MouseRBtnUpNotify_EV.html).

## Remarks

If developing a C++ application, use [swMouseRBtnUpNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
